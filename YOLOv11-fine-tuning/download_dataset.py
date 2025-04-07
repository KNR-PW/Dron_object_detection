from roboflow import Roboflow
rf = Roboflow(api_key="API_KEY")
project = rf.workspace("roboflow-100").project("construction-safety-gsnvb")
version = project.version(2)
dataset = version.download("yolov11")
                
                
