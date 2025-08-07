from ultralytics import YOLO
# Load 
model = YOLO("yolov8n-cls.pt")
# train
results = model.train(data="C:\\Users\\ASUS\\OneDrive\\Desktop\\swaccha-connect\\dataset", epochs=120,  imgsz=224)


