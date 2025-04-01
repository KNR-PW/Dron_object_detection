###############################__YOLO__###############################
GIGA FAJNA STRONA:
https://www.ultralytics.com

DO YOLOv5:
https://docs.ultralytics.com/yolov5/

DO YOLOv8:
https://docs.ultralytics.com/models/yolov8/#performance-metrics

DO YOLOv11:
https://docs.ultralytics.com/models/yolo11/#performance-metrics

Do treningu potrzebne są modele yolo od nano (n) do extra large (xl)
!!!! UŻYCIE WIĘKSZYCH MODELI WIAŻE SIE Z USTAWIENIEM ODPOWIEDNICH PARAMETRÓW ZUŻYCIA NA KARCIE GRAFICZNEJ !!!!

###############################__DATASETS__###############################

STRONA ZE ZBIOREM DANYCH:
https://universe.roboflow.com

STRUKTURA DANYCH DLA YOLO: (FORMAT DLA DANEJ WERSJI YOLO, database na yv8 może nie działać na yv11)

- ZBIÓR DANYCH (bottle)
    - test
        - images
            - pic1.jpg
            - pic2.jpg
        - labels
            - annotations_for_pic1.txt
            - annotations_for_pic2.txt
    - train
        - images
            - pic1.jpg
            - pic2.jpg
        - labels
            - annotations_for_pic1.txt
            - annotations_for_pic2.txt
    - valid
        - images
            - pic1.jpg
            - pic2.jpg
        - labels
            - annotations_for_pic1.txt
            - annotations_for_pic2.txt


PO POMYŚLNYM TRENINGU TWORZY SIĘ FOLDER RUNS Z DANYNMI TRENINGU ORAZ PLIK trained_model_yolov_nr.wersji.pt

###############################__KONWERSJA_MODELU_PyTorch_NA_ONNX_NA_HAILO__###############################

ŻEBY AI HAT NA RASPBERRY PI DZIAŁAŁ DOBRZE TRZEBA SKONFIGUROWAC
Link: https://www.raspberrypi.com/documentation/accessories/ai-hat-plus.html 
(PS działa na pewno)
