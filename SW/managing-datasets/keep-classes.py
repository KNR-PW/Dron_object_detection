import os
import argparse

parser = argparse.ArgumentParser(description="Keeps labels and images with specific classes (or empty) and removes unwanted class lines from labels.")
parser.add_argument("dataset_path", type=str, help="Path to folder containing train, test, valid directories")
parser.add_argument("--keep", nargs="+", type=int, required=True, help="List of class IDs to keep (e.g. --keep 0 1)")

args = parser.parse_args()
keep_classes = set(args.keep)
dataset_path = os.path.expanduser(args.dataset_path)

datasets = ["train", "test", "valid"]

for dataset in datasets:
    labels_dir = os.path.join(dataset_path, dataset, "labels")
    images_dir = os.path.join(dataset_path, dataset, "images")

    if not os.path.exists(labels_dir) or not os.path.exists(images_dir):
        print(f"⚠️ Skipped: {labels_dir} or {images_dir} not found.")
        continue

    for label_file in os.listdir(labels_dir):
        if not label_file.endswith(".txt"):
            continue

        label_path = os.path.join(labels_dir, label_file)
        image_path_jpg = os.path.join(images_dir, label_file.replace('.txt', '.jpg'))
        image_path_png = os.path.join(images_dir, label_file.replace('.txt', '.png'))

        with open(label_path, "r") as f:
            lines = f.readlines()

        # Separate lines into keepable and discardable
        keep_lines = [line for line in lines if int(line.split()[0]) in keep_classes]
        is_empty = len(lines) == 0
        has_keepable = len(keep_lines) > 0

        # Decide action: keep or delete
        if is_empty or has_keepable:
            # Overwrite file with filtered lines (if not empty)
            if keep_lines:
                with open(label_path, "w") as f:
                    f.writelines(keep_lines)
            else:
                # If empty, just leave it as is (still useful in training)
                open(label_path, "w").close()
        else:
            try:
                os.remove(label_path)
            except Exception as e:
                print(f"⚠️ Error removing label {label_path}: {e}")

            if os.path.exists(image_path_jpg):
                try:
                    os.remove(image_path_jpg)
                except Exception as e:
                    print(f"⚠️ Error removing image {image_path_jpg}: {e}")
            elif os.path.exists(image_path_png):
                try:
                    os.remove(image_path_png)
                except Exception as e:
                    print(f"⚠️ Error removing image {image_path_png}: {e}")

print("✅ Filtering complete.")
