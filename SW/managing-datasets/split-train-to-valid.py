import os
import random
import shutil
import argparse
from tqdm import tqdm

def move_files(image_files, src_img_dir, src_lbl_dir, dst_img_dir, dst_lbl_dir):
    os.makedirs(dst_img_dir, exist_ok=True)
    os.makedirs(dst_lbl_dir, exist_ok=True)

    for img_file in tqdm(image_files, desc="Moving to valid"):
        label_file = os.path.splitext(img_file)[0] + ".txt"

        src_img = os.path.join(src_img_dir, img_file)
        src_lbl = os.path.join(src_lbl_dir, label_file)

        dst_img = os.path.join(dst_img_dir, img_file)
        dst_lbl = os.path.join(dst_lbl_dir, label_file)

        if os.path.exists(src_lbl):
            shutil.move(src_img, dst_img)
            shutil.move(src_lbl, dst_lbl)
        else:
            print(f"⚠️ Missing label for image: {img_file}, skipping.")

def main():
    parser = argparse.ArgumentParser(description="Moves a percentage of train/ data to valid/")
    parser.add_argument("dataset_path", type=str, help="Path to dataset directory")
    parser.add_argument("--percent", type=float, default=0.15, help="Percentage of training data to move (default: 0.15)")

    args = parser.parse_args()

    if not (0 < args.percent <= 1):
        print("❌ Error: --percent must be a float between 0 and 1 (e.g. 0.15 for 15%)")
        return

    base_dir = os.path.abspath(args.dataset_path)
    train_img_dir = os.path.join(base_dir, "train", "images")
    train_lbl_dir = os.path.join(base_dir, "train", "labels")
    valid_img_dir = os.path.join(base_dir, "valid", "images")
    valid_lbl_dir = os.path.join(base_dir, "valid", "labels")

    if not os.path.isdir(train_img_dir) or not os.path.isdir(train_lbl_dir):
        print("❌ Folder train/images or train/labels not found.")
        return

    image_files = [f for f in os.listdir(train_img_dir) if f.lower().endswith((".jpg", ".png"))]
    if not image_files:
        print("❌ No image files found in train/images.")
        return

    sample_size = max(1, int(args.percent * len(image_files)))
    valid_samples = random.sample(image_files, sample_size)

    #print(f"📦 Moving {sample_size} image-label pairs from train to valid...")
    move_files(valid_samples, train_img_dir, train_lbl_dir, valid_img_dir, valid_lbl_dir)
    print("✅ Split complete.")

if __name__ == "__main__":
    main()
