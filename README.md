# Data Privacy Project

A Python-based data privacy workflow that automatically processes input images, detects sensitive objects using a YOLOv8 object detection model, and applies privacy-preserving modifications (such as blurring) to protect identity and personal data.

## 🛠️ Features
* **Automated Pipeline**: Imports source images seamlessly.
* **YOLOv8 Integration**: Uses the lightweight `yolov8n.pt` model weights for fast, real-time object/face detection.
* **Privacy Controls**: Automatically generates protected output images with sensitive regions obfuscated.

## 📁 Repository Structure
* `privacy_pipeline.py` — The core Python script managing the detection and processing loop.
* `yolov8n.pt` — Pre-trained Ultralytics YOLOv8 nano model weights.
* `image.jpg` — Sample input testing image.
* `output_privacy.jpg` — Resulting anonymized output image.

## 🚀 Getting Started

### Prerequisites
Make sure you have Python installed, then install the required dependencies:
```bash
pip install ultralytics opencv-python
```

### Running the Pipeline
Execute the main script to process your images:
```bash
python privacy_pipeline.py
```

## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.
