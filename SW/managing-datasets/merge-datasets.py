import os
import sys
import shutil

def create_dataset_structure(target_path):
    for subset in ["train", "test", "valid"]:
        for folder in ["images", "labels"]:
            os.makedirs(os.path.join(target_path, subset, folder), exist_ok=True)

def extract_unique_classes(target_path):
    class_ids = set()
    for subset in ["train", "test", "valid"]:
        labels_dir = os.path.join(target_path, subset, "labels")
        if not os.path.exists(labels_dir):
            continue
        for file in os.listdir(labels_dir):
            if not file.endswith(".txt"):
                continue
            with open(os.path.join(labels_dir, file), "r") as f:
                for line in f:
                    parts = line.strip().split()
                    if parts:
                        try:
                            class_ids.add(int(parts[0]))
                        except ValueError:
                            continue
    return sorted(class_ids)

def create_data_yaml(target_path):
    class_ids = extract_unique_classes(target_path)
    nc = len(class_ids)
    placeholder_names = [f"'class_{i}'" for i in range(nc)]
    content = f"""train: ../train/images
val: ../valid/images
test: ../test/images

nc: {nc}
names: [{', '.join(placeholder_names)}]  # <- Replace with actual class names
"""
    with open(os.path.join(target_path, "data.yaml"), "w") as f:
        f.write(content)
    print(f"📝 Created data.yaml with nc={nc}")

def copy_dataset_content(source, target):
    for subset in ["train", "test", "valid"]:
        for folder in ["images", "labels"]:
            src_dir = os.path.join(source, subset, folder)
            dst_dir = os.path.join(target, subset, folder)
            if not os.path.exists(src_dir):
                continue
            for file in os.listdir(src_dir):
                shutil.copy2(os.path.join(src_dir, file), os.path.join(dst_dir, file))

def main():
    if len(sys.argv) != 3:
        print("❌ Usage: python3 merge-datasets.py /path/to/datasets merged_dataset_name")
        sys.exit(1)

    datasets_path = os.path.abspath(sys.argv[1])
    target_name = sys.argv[2]
    target_path = os.path.join(datasets_path, target_name)

    if not os.path.isdir(datasets_path):
        print(f"❌ Provided path is not a directory: {datasets_path}")
        sys.exit(1)

    os.makedirs(target_path, exist_ok=True)
    create_dataset_structure(target_path)

    dataset_folders = [
        d for d in os.listdir(datasets_path)
        if os.path.isdir(os.path.join(datasets_path, d)) and d != target_name
    ]

    if not dataset_folders:
        print("⚠️ No datasets found to merge.")
        return

    for folder in dataset_folders:
        print(f"🚚 Merging: {folder}")
        copy_dataset_content(os.path.join(datasets_path, folder), target_path)

    create_data_yaml(target_path)
    print("✅ Merge complete at:", target_path)

if __name__ == "__main__":
    main()
