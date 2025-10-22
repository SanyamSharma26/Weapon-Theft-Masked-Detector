# Weapon & Theft Masked Detector (YOLOv8)

## Abstract

This project implements a real-time object detection system designed to identify weapons and detect theft-related behavior, while also recognizing masked faces/people in surveillance imagery. The core detection model is based on the YOLOv8 architecture and is implemented in Python. The primary goal is to provide a lightweight, accurate detector suitable for security and surveillance applications where timely alerts and visual evidence are required.

## Objectives

- Detect the presence of weapons in images and video frames
- Detect theft-related scenarios (e.g., masked faces, weapons etc) where applicable
- Recognize and locate people (including masked individuals) in the scene
- Produce bounding boxes and confidence scores for detections suitable for downstream alerting and logging

## Dataset

- **Total images:** 4,579
- **Annotations:** People are annotated using the YOLOv8 annotation format (class ids + normalized bounding boxes)
- **Notes:** Dataset contains scenes representative of surveillance environments, including variations in pose, occlusion, lighting, and use of face masks

## Pre-processing

Each image in the dataset received the following pre-processing steps prior to training:

1. **Auto-orientation of pixel data** — Images were rotated according to EXIF orientation tags where present; EXIF orientation metadata was stripped after correction
2. **Resize to 640×640 (stretch)** — All images were resized to a fixed 640×640 resolution (No aspect-ratio preserving padding was applied; images were stretched to fit)

## Annotation Format

Annotations follow the YOLOv8 format: each image has an associated text file with lines containing:

```
class_id x_center y_center width height
```

where values are normalized to image width and height.

## Model and Implementation (High Level)

- **Model architecture:** YOLOv8 (object detection model family)
- **Implementation language:** Python
- **Purpose:** Train a detection model capable of locating weapons and people in single images or individual video frames
- **Notes:** Implementation focuses on detection accuracy and inference speed suitable for near real-time processing on commodity hardware

## Training Overview

- **Train/validation split:** A standard approach is recommended (e.g., 80/20 or 85/15) unless an alternative split is required by the evaluation protocol
- **Loss & optimization:** Use YOLOv8's built-in loss and optimizer defaults for steady convergence unless further tuning is needed
- **Batching & resolution:** Training at 640×640 resolution to match pre-processing; batch size and number of epochs depend on available compute and desired performance

## Outputs & Integrations

Typical outputs that can be integrated into a larger system:

- Bounding boxes, class labels, and confidence scores per detection
- Timestamped logs of events (for storage and audit trails)
- Event-triggered alerts (SMS, push, email) when weapon or theft is detected above a confidence threshold
- Visual evidence (cropped frames) for human review and legal records

## Ethical & Legal Considerations

- **Privacy:** Deploying people-detection systems in public or private spaces must comply with applicable privacy laws and regulations. Always confirm legal requirements and obtain necessary consents
- **Bias & fairness:** Ensure the dataset does not unduly bias detection performance across demographic groups or environments. Validate performance across representative subsets
- **Responsible use:** Use detection results as indicators requiring human verification rather than as sole evidence of wrongdoing

---
