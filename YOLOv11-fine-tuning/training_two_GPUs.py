from ultralytics import YOLO
import torch
from multiprocessing import freeze_support

if __name__ == '__main__':
    freeze_support()

    print("GPU Available:", torch.cuda.is_available())
    num_gpus = torch.cuda.device_count()
    print("Number of GPUs:", num_gpus)
    for i in range(num_gpus):
        print(f"GPU {i} Name:", torch.cuda.get_device_name(i))

    # Load the YOLO model (adjust the model path as needed)
    model = YOLO("yolo11n.pt")

    # Train the model on the dataset for 200 epochs using both GPUs
    results = model.train(
        data="/home/ai/YOLOv11n-fine-tuning/construction-safety-2/data.yaml",
        epochs=200,
        imgsz=640,
	batch=150,
        device="0,1",  # Run on both GPU 0 and GPU 1
        name="train"
    )

    # Evaluate model performance on the validation set
    metrics = model.val()

    # Perform object detection on an image
    results = model("/home/ai/YOLOv11n-fine-tuning/construction-safety-2/test/images/ppe_0004_jpg.rf.c3265071237f64a4f0c3e1bf3048f923.jpg")
    results[0].show()

    # Export the model to ONNX format
    path = model.export(format="pt")  # Returns path to the exported model
