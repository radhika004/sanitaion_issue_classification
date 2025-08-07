from ultralytics import YOLO
import numpy as np
model = YOLO("runs\\classify\\train18\\weights\\best.pt")  
results = model("C:\\Users\\ASUS\\OneDrive\\Desktop\\swaccha-connect\\images (4).jpg")
# results = model("C:\\Users\\ASUS\\OneDrive\\Desktop\\swaccha-connect\\images (3).jpg")
names_dict = results[0].names

probs = results[0].probs.tolist()
print(names_dict)
print(probs)

print(names_dict[np.argmax(probs)])
