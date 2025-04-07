## FILES-FILTER.PY
Keeps labels and corresponding images that either own specified classes (`--classes`) or have no class at all.
Deletes all other files.
```bash
python3 files-filter.py /path/to/dataset --classes class_id_1 class_id_2
```

## CLASS-FILTER.PY
Remaps one `class_id` to another in label files. Before remapping, it first deletes the target class (i.e., if mapping `2:1`, it will first remove class `1` and then convert class `2` into `1`).
By default, it deletes all other classes as well, but you can use `--keep` to preserve classes that are not involved in remapping.
```bash
python3 class-filter.py /path/to/dataset --map old1:new1 old2:new2 --keep class1 class2
```