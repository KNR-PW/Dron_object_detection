# Yolo

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

# Data

Link to docs with datasets:
https://docs.google.com/document/d/1wU16wfVyw3NkAwoQJrEnreeYpgM6BZ6omETgWTGLDKQ/edit?usp=sharing

https://universe.roboflow.com/

## 

# Szymon datasets

````
Link to docs with datasets:
https://docs.google.com/document/d/1wU16wfVyw3NkAwoQJrEnreeYpgM6BZ6omETgWTGLDKQ/edit?usp=sharing

https://universe.roboflow.com/

The DATASET and individual datasets are already filtered and prepared. They share the following common classes:
```bash
nc: 3
names: ['Human', 'Safety vest', 'Hardhat']
```

## Human
https://universe.roboflow.com/lifesparrow/images-25-8

https://universe.roboflow.com/xx-nnenm/ins2-yqvsv

https://universe.roboflow.com/dipto-sarkar/merge1-thsaj

https://universe.roboflow.com/taskforceswarm/personfinder-ewfix

*
https://universe.roboflow.com/kyawyeaung/small-objects_111111

https://universe.roboflow.com/alex-eagles-5-m/suas-mannequin-detection

https://universe.roboflow.com/sih-p7hel/toiletdetection

https://universe.roboflow.com/ttttt-pxiqn/w-dh28y

https://universe.roboflow.com/new-workspace-eiscf/yolov5persondetector


## Safety Vest + Hardhat
https://universe.roboflow.com/roboflow-universe-projects/construction-site-safety

# also human, but delete if trouble from high altitude
https://universe.roboflow.com/roboflow-universe-projects/personal-protective-equipment-combined-model

# also human, same as above
https://universe.roboflow.com/ruisong-zheng-ic9t9/ppe-3.16

# only Safety vest
https://universe.roboflow.com/roboflow-universe-projects/safety-vests

# only Hardhat
https://universe.roboflow.com/universe-datasets/hard-hat-universe-0dy7t

# only Safety vest
https://universe.roboflow.com/filubels/deeplope


## Fence
https://universe.roboflow.com/new-workspace-pmocx/fence-holes

https://universe.roboflow.com/cvproject-wentv/hunter_fenceline

https://universe.roboflow.com/3modelstraining/bentfence

https://universe.roboflow.com/uji-thesis/broken-fence-detection-v2

https://universe.roboflow.com/ia2-jtond/br-bhfsx

https://universe.roboflow.com/uji-thesis/broken-fence-detection

## Power line
https://universe.roboflow.com/bistu/powerline-c7pls

https://universe.roboflow.com/hughes-perreault-5ivvo/power-lines-rozvy

https://universe.roboflow.com/bdpc-ai-gd2/dt-day-dan-tran

https://universe.roboflow.com/objdetection-b0lfu/powerline-fault-detection-upvfb //!!!

https://universe.roboflow.com/indian-institute-of-technology-jodhpour/wire-detection-qeaxa 

https://universe.roboflow.com/vipin-ap-g3oap/poles-detetct

https://universe.roboflow.com/bdpc-ai-gd2/dt-day-dan-boc-tt

https://universe.roboflow.com/branchpowerline-xsenh/powerline-seg

## Utility pole 
https://universe.roboflow.com/ghost-gsj7h/ghost04-pole

https://universe.roboflow.com/workspace-sfj9d/postes-urbanos //??

https://universe.roboflow.com/new-workspace-en1on/utility-pole-label

https://universe.roboflow.com/abduljalil/pole_detection-ehhzv

https://universe.roboflow.com/sur-496-research/nc-roadway-features //utility pole + power line, though I’d be wary with this one

## Pipeline
https://universe.roboflow.com/utp-jtbn5/pipeline-tracks

https://universe.roboflow.com/reconocimiento-de-fugas/pipeline-detect-jg2bt

https://universe.roboflow.com/truck-x0dsl/pipeline-tracks-2-0msrc

https://universe.roboflow.com/jaehak/crack-segmentation-zgvrg //cracks

https://universe.roboflow.com/skander/object-segmentation-vvi1g //more cracks

https://universe.roboflow.com/crack-7rsjb/crack-detection-ol3yi //even more cracks

https://universe.roboflow.com/sheraz505/pipeline-leak-prediction-ouuy0 //pipeline leaks

https://universe.roboflow.com/sayali-8lu3k/uycgha //crapton of cracks

https://universe.roboflow.com/zbxxx/burst-kxutb-nbb28 //bursts

https://universe.roboflow.com/krum-dala/pipe-defects-ybzjr //pipe defects

https://universe.roboflow.com/zbxxx/pipe-leak //leaksss

https://universe.roboflow.com/pipe-leak/pipe-leak-yshqq //more leaks 

## Rust
https://universe.roboflow.com/practice-9ogyy/abc-h0rah

https://universe.roboflow.com/omar-el-ghati-1f4cz/rust-seg 

https://universe.roboflow.com/faisal-hazry-orm7q/yolov8corrosion 

https://universe.roboflow.com/ibm-puugd/mess_oxidation 

https://universe.roboflow.com/kiot-utdwr/rust-vmwoa 

https://universe.roboflow.com/guna-fyoeu/rust_detection-tyqyi

https://universe.roboflow.com/defectdetection-qdxvy/corrosion-of-automation-ioqzy 




## Car/pallet


## Worker(helmet or vest)
## Worker(without helmet and vest)
## Fire
````
