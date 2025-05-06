import os
import argparse

# Konfiguracja argumentów
parser = argparse.ArgumentParser(description="Przekształca ID klas w plikach YOLO labels zgodnie z mapowaniem.")
parser.add_argument("dataset_path", type=str, help="Ścieżka do folderu zawierającego train, test, valid")
parser.add_argument("--map", nargs="+", required=True, help="Lista zamian klas w formacie old:new, np. 2:1 4:0")

args = parser.parse_args()
dataset_path = os.path.expanduser(args.dataset_path)

# Parsowanie mapy
mapa_klas = {}
for mapping in args.map:
    old, new = map(int, mapping.split(":"))
    mapa_klas[old] = new

# Lista folderów do sprawdzenia
datasets = ["train", "test", "valid"]

for dataset in datasets:
    labels_dir = os.path.join(dataset_path, dataset, "labels")
    if not os.path.exists(labels_dir):
        print(f"⚠️ Pominięto: {labels_dir} nie istnieje.")
        continue

    for label_file in os.listdir(labels_dir):
        if not label_file.endswith(".txt"):
            continue

        label_path = os.path.join(labels_dir, label_file)
        new_lines = []

        with open(label_path, "r") as file:
            for line in file:
                parts = line.strip().split()
                if not parts:
                    continue  # pomiń puste linie
                class_id = int(parts[0])
                rest = parts[1:]
                # Zamień klasę, jeśli jest na liście
                class_id = mapa_klas.get(class_id, class_id)
                new_lines.append(f"{class_id} {' '.join(rest)}")

        with open(label_path, "w") as file:
            file.write("\n".join(new_lines) + "\n")

print("✅ Przekształcanie klas zakończone.")
