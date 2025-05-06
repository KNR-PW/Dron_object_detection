from ultralytics import YOLO
import torch
from multiprocessing import freeze_support
import os
script_dir = os.path.dirname(os.path.abspath(__file__))

# path to datasets yaml file
dataset_folder_path = " "
test_image_path = " "
data_yaml_path = os.path.join(script_dir, dataset_folder_path)
model_size = "n" #n,s,m
batch = 10 # how much vram do you have? size 150 for 48GB


def set_device():
    '''
    Fun to set computing device depending on the amount(1 or 2) GPUs or no GPU - using cpu
    '''
    # print("GPU Available:", torch.cuda.is_available())
    # check% if and how much gpus there are
    num_gpus = torch.cuda.device_count()
    if num_gpus == 0:
        device = "cpu"
        print("\033[91mno GPU switching to CPU\033[0m")
    elif num_gpus == 1:
        device = "0"
        print(f"\033[94mone GPU with {torch.cuda.get_device_properties(0).total_memory / 1e9:.1f} GB vRAM\033[0m")
    elif num_gpus == 2:
        device = "0,1"
        combined_vram = (torch.cuda.get_device_properties(0).total_memory + torch.cuda.get_device_properties(1).total_memory) / 1e9
        print(f"\033[94mtwo GPUs with {combined_vram:.1f} GB vRAM\033[0m")
    return device

if __name__ == '__main__':
    freeze_support()

    device = set_device()
    model = YOLO(f"yolo11{model_size}.pt")

    # Train the model on the dataset for 200 epochs using both GPUs
    results = model.train(
        data=data_yaml_path,
        epochs=200,
        imgsz=640,
        batch=batch,
        device=device,
        name="train"
    )

    # Evaluate model performance on the validation set
    metrics = model.val()

    # Perform object detection on an image
    results = model(test_image_path)
    results[0].show()

    # Export the model to ONNX format
    path = model.export(format="pt")  # Returns path to the exported model
