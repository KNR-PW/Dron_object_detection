import gdown
import zipfile
import os

datasets = [
    {
        "file_id": "1TpkNs21A1upqWDDAJwWBDxZA3MD6o4c8",
        "output": "dataset_maly.zip",
        "extract_to": "datasets"
    },
    {
        "file_id": "1CaszzY-AVyGOtYGB-JApujM3h83EdtbW",
        "output": "dataset_duzy.zip",
        "extract_to": "datasets"
    }
]

for ds in datasets:
    url = f"https://drive.google.com/uc?id={ds['file_id']}"
    print(f"⬇️  Downloading {ds['output']}...")
    gdown.download(url, ds['output'], quiet=False)

    print(f"📦 Extracting {ds['output']} to {ds['extract_to']}...")
    os.makedirs(ds['extract_to'], exist_ok=True)
    with zipfile.ZipFile(ds['output'], 'r') as zip_ref:
        zip_ref.extractall(ds['extract_to'])

print("✅ Wszystkie zbiory zostały pobrane i rozpakowane.")