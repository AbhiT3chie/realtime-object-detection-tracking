# Realtime Object Detection & Tracking

Real-time object detection and tracking system using YOLOv8 and OpenCV, 
built for exploring computer vision applications in dynamic environments 
like gaming and interactive systems.

## Demo
<img width="847" height="717" alt="WhatsApp Image 2026-07-11 at 4 02 49 PM" src="https://github.com/user-attachments/assets/eed5a5a5-3aa8-4160-8ca7-fa75a29235ab" />


## Tech Stack
- Python
- OpenCV
- YOLOv8 (Ultralytics)

## Features
- Real-time object detection via webcam feed
- Multi-object tracking across frames
- Live bounding box + label visualization

## Setup
\`\`\`bash
pip install ultralytics opencv-python
python detect_track.py
\`\`\`

## How it Works
Uses YOLOv8's pretrained model for detection, combined with its built-in 
tracker to maintain object identity across frames.
