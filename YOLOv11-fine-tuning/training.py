from ultralytics import YOLO
import torch
from multiprocessing import freeze_support

if __name__ == '__main__':
    freeze_support()

    print("GPU Available: ", torch.cuda.is_available())
    print("GPU Name: ", torch.cuda.get_device_name(0))

    # Load a COCO-pretrained YOLO11n model
    model = YOLO("yolo11n.pt")

    # Train the model on the COCO8 example dataset for 100 epochs
    results = model.train(
            data="/home/ai/YOLOv11n-fine-tuning/construction-safety-2/data.yaml",
        epochs=200, 
        imgsz=640,
        device=0,
        name="train"
        )
    
    # Evaluate model performance on the validation set
    metrics = model.val()

    # Perform object detection on an image
    results = model("YOUR_TESTING_IMAGE_PATH_HERE")
    results[0].show()

    # Export the model to ONNX format
    path = model.export(format="onnx")  # return path to exported model
