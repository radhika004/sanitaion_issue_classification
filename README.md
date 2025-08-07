
# 🧠 YOLOv8 Image Classification for SwachhConnect

This repository contains the YOLOv8-based image classification module for the **SwachhConnect** project — an AI-powered civic issue detection platform. The classifier automatically detects issues such as garbage dumps, potholes, drainage problems, and dead animals from user-submitted images.

## 📌 Overview

We trained a custom YOLOv8 classification model (`YOLOv8n`) on a manually curated dataset of 6 classes representing common civic issues. This classifier is integrated into the backend system of SwachhConnect to auto-label images during complaint submission.

## 🗂️ Dataset Preparation

- Collected images using Bing Image Downloader and field submissions.
- Classes: `Garbage`, `Potholes`, `Drainage`, `Dead Animals`, etc.
- Performed image cleaning, duplicate removal, resizing, and structured data into class-wise folders.
- Total images: ~1120 (train/test split used)

## 🧠 Model Training

- Model Used: **YOLOv8n (nano)** for image classification
- Training Epochs: Initially 60, then extended to 100 (early stopped at 77)
- Folder Structure: Follows Ultralytics' format for classification
- Training Command:
  ```bash
  yolo classify train data=dataset.yaml model=yolov8n-cls.pt epochs=100 imgsz=224
  ```

## 📊 Evaluation Results

After training, the model was evaluated on a separate test set using `app3.py`:

```
Accuracy: 0.7549
Precision: 0.7827
Recall: 0.7549
F1 Score: 0.7408
```

## 🔍 Model Inference Script (`app3.py`)

The script:
- Loads the trained model (`best.pt`)
- Iterates over test images in class-wise folders
- Predicts image class and compares with ground truth
- Outputs classification metrics (Accuracy, Precision, Recall, F1 Score)

## 🧰 Tech Stack

- YOLOv8 (Ultralytics)
- Python, OpenCV, PIL
- scikit-learn, NumPy

## 🏁 How to Run

1. Place your model weights in: `runs/classify/train22/weights/best.pt`
2. Prepare your test image folder: `test_images/class_name/image.jpg`
3. Run the evaluation script:
   ```bash
   python app3.py
   ```

## 📦 Output

category of the image (garbage,pathhole,etc)

---
