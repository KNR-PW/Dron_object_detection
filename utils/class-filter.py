import os
import argparse

# Konfiguracja argumentów
parser = argparse.ArgumentParser(description="Zamienia ID klas w YOLO labels i opcjonalnie filtruje niepotrzebne obiekty.")
parser.add_argument("dataset_path", type=str, help="Ścieżka do folderu zawierającego train, test, valid")
parser.add_argument("--map", nargs="+", required=True, help="Lista zamian klas w określonej kolejności, np. 1:3 2:1")
parser.add_argument("--keep", nargs="+", type=int, default=None, help="Lista klas do zachowania (opcjonalnie)")

args = parser.parse_args()
dataset_path = os.path.expanduser(args.dataset_path)  # Obsługa `~` w ścieżce

# **Tworzymy mapę zamian W PODANEJ KOLEJNOŚCI**
mapa_klas = []
for mapping in args.map:
    old, new = map(int, mapping.split(":"))
    mapa_klas.append((old, new))

# **Usuwamy klasy docelowe, ale NIE usuwamy źródłowych!**
klasy_do_usuniecia = {new for _, new in mapa_klas}  # Tylko wartości docelowe

# **Zestaw dozwolonych klas**
if args.keep is not None:
    dozwolone_klasy = set(args.keep) | {old for old, _ in mapa_klas} | {new for _, new in mapa_klas}
else:
    # Jeśli `--keep` NIE jest podane, to zachowujemy tylko klasy występujące w `--map`
    dozwolone_klasy = {old for old, _ in mapa_klas} | {new for _, new in mapa_klas}

# Lista folderów do sprawdzenia
datasets = ["train", "test", "valid"]

# Przetwarzanie każdego zestawu folderów
for dataset in datasets:
    labels_dir = os.path.join(dataset_path, dataset, "labels")

    if not os.path.exists(labels_dir):
        print(f"Pominięto: {labels_dir} nie istnieje.")
        continue

    for label_file in os.listdir(labels_dir):
        label_path = os.path.join(labels_dir, label_file)

        if not label_file.endswith('.txt'):
            continue

        temp_wiersze = []

        # **Krok 1: Wczytanie pliku i usunięcie docelowych klas**
        with open(label_path, "r") as file:
            for line in file:
                dane = line.split()
                klasa = int(dane[0])

                # **Usuwamy tylko klasy docelowe (czyli `new` w `--map`), ale NIE usuwamy `old`**
                if klasa in klasy_do_usuniecia and klasa not in [old for old, _ in mapa_klas]:
                    continue  

                temp_wiersze.append((klasa, dane[1:]))

        # **Krok 2: Zamiana klas zgodnie z KOLEJNOŚCIĄ argumentów**
        for i, (klasa, reszta) in enumerate(temp_wiersze):
            for old, new in mapa_klas:
                if klasa == old:
                    klasa = new  # Dokładna kolejność zamian
            temp_wiersze[i] = (klasa, reszta)

        # **Krok 3: Filtrowanie dozwolonych klas**
        nowe_wiersze = [
            f"{klasa} " + " ".join(reszta) for klasa, reszta in temp_wiersze if klasa in dozwolone_klasy
        ]

        # **Zapisujemy zmieniony plik**
        with open(label_path, "w") as file:
            file.write("\n".join(nowe_wiersze) + "\n")

print("Przetwarzanie zakończone!")

# DOMYŚLNIE, wszystkie klasy, które nie są wymienione za pomocą --keep lub które nie są wynikiem --map, są USUWANE !!!
# ⚠️ NIE możemy naraz robić zamiany, tak, że klasa jest używana w dwóch miejscach !!!
# ⚠️ PAMIĘTAĆ, ŻE PRZY wielokrotnej manipulacji klasami,, trzeba pamięrać aby poprzednio zamienione klasy UMIEŚCIĆ w --keep
#SZCZEGÓLNY PRZYPADEK, wzajemna zamiana klas, np. 1<->2 (1 na 2 ORAZ 2 na 1)
#Jeśli chcemy zamienić 2->1 i 1->2,, to NAJPIERW --map 1:3 --keep 2 (klasa 3 będzie naszą zmienną 'tymczasową')
#Potem:: --map 2:1 --keep 3
#Na koniec:: --map 3:2 --keep 1
#W TEN SPOSÓB zamieniamy klasy WZAJEMNIE !!!! (przykład jeśli zależy nam tylko na tych dwóch klasach !!)