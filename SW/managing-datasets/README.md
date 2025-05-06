
How to deal with new dataset:::
1.Use 'keep-classes' to filter your dataset's classes
2.Use 'remap-classes' to change 'class_id'
3.Use 'split-train-to-valid' to split a portion of training data into the validation set, keeping a preferred train/valid ratio


## KEEP-CLASSES.PY
Keeps labels and corresponding images that either own specified classes (`--keep`) or have no class at all.
Deletes all other files and the description of the classes in labels that weren't mentioned in (`--keep`).
```bash
python3 keep-classes.py /path/to/dataset --keep class_id_1 class_id_2
```

## REMAP-CLASSES.PY
Remaps one `class_id` to another in label files.
```bash
python3 remap-classes.py /path/to/dataset --map old1:new1 old2:new2
```

## SPLIT-TRAIN-TO-VALID.PY
Moves a percentage of image-label pairs from the train/ split to the valid/ split.
Automatically creates valid/ directories if missing, or adds to them if already present.
```bash
python3 split-train-to-valid.py /path/to/dataset --percent 0.15
```
--percent (optional) – float between 0 and 1 indicating the portion of training data to move (default: 0.15 = 15%).

## MERGE-DATASETS.PY
Merges multiple YOLO datasets located in the current directory into one target dataset.
Copies all files from train, test, and valid subfolders (under images/ and labels/) from each dataset (except the target one).
Creates the target dataset folder with the correct structure and a placeholder data.yaml file for manual class description.
```bash
python3 merge-datasets.py /path/to/datasets merged_dataset_name
```
```bash
train: ../train/images
val: ../valid/images
test: ../test/images

nc: 4  # <-- automatical detection
names: [ 'CLASS_0', 'CLASS_1', 'CLASS_2', 'CLASS_3' ]  # <-- manual class description
```