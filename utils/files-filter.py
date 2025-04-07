import os
import argparse

# Konfiguracja argumentów
parser = argparse.ArgumentParser(description="Filtruje pliki labels i images w folderach train, test, valid")
parser.add_argument("dataset_path", type=str, help="Ścieżka do folderu zawierającego train, test, valid")
parser.add_argument("--classes", nargs="+", type=int, required=True, help="Lista interesujących klas (np. --classes 0 1)")

args = parser.parse_args()
interesujace_klasy = set(args.classes)
dataset_path = os.path.expanduser(args.dataset_path)  # Obsługa ~ w ścieżce

# Lista folderów do sprawdzenia
datasets = ["train", "test", "valid"]

# Przetwarzanie każdego zestawu folderów
for dataset in datasets:
    labels_dir = os.path.join(dataset_path, dataset, "labels")
    images_dir = os.path.join(dataset_path, dataset, "images")

    # Sprawdzenie, czy oba foldery istnieją
    if not os.path.exists(labels_dir) or not os.path.exists(images_dir):
        print(f"⚠️ Pominięto: {labels_dir} lub {images_dir} nie istnieje.")
        continue

    # Przetwarzanie plików w labels
    for label_file in os.listdir(labels_dir):
        label_path = os.path.join(labels_dir, label_file)
        image_path = os.path.join(images_dir, label_file.replace('.txt', '.jpg'))

        # Sprawdzenie, czy plik jest .txt
        if not label_file.endswith('.txt'):
            continue

        # Flaga informująca, czy znaleziono interesującą klasę
        znaleziono_interesujaca_klase = False
        is_empty = True  # Flaga dla pustych plików

        # Odczytanie zawartości pliku .txt
        with open(label_path, "r") as file:
            for line in file:
                is_empty = False  # Plik nie jest pusty
                class_id = int(line.split()[0])
                if class_id in interesujace_klasy:
                    znaleziono_interesujaca_klase = True
                    break

        # Jeśli plik nie zawiera interesujących klas i nie jest pusty, usuń go i odpowiadający obraz
        if not znaleziono_interesujaca_klase and not is_empty:
            try:
                os.remove(label_path)
            except Exception as e:
                print(f"⚠️ Błąd przy usuwaniu TXT {label_path}: {e}")

            if os.path.exists(image_path):
                try:
                    os.remove(image_path)
                except Exception as e:
                    print(f"⚠️ Błąd przy usuwaniu obrazu {image_path}: {e}")

print("Filtracja zakończona!")
