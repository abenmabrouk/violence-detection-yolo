# Violence Detection using YOLOv8

## Overview

This project aims to build a complete computer vision pipeline for automatic violence detection in surveillance videos.

Instead of directly training a deep learning classifier, the project first extracts meaningful behavioral features from tracked persons, following a modular research-oriented approach.

---

## Current Features

### Detection
- Person detection using YOLOv8

### Multi-object Tracking
- ByteTrack integration
- Persistent object IDs
- Trajectory history

### Motion Analysis
- Speed estimation
- Motion direction
- Motion angle
- Acceleration estimation
- Distance traveled

### Interaction Analysis
- Pairwise distance computation
- Close-contact detection
- Local crowd density estimation

### Visualization
- Bounding boxes
- Object IDs
- Motion vectors
- Trajectories
- Interaction links
- Real-time annotations

---

## Project Architecture

```
Video
   │
   ▼
YOLOv8 Detection
   │
   ▼
ByteTrack Tracking
   │
   ▼
Motion Analysis
   │
   ▼
Interaction Analysis
   │
   ▼
Behavior Analysis (Coming Soon)
   │
   ▼
Violence Detection (Coming Soon)
```

---

## Project Structure

```
src/
│
├── config.py
├── detector.py
├── drawing.py
├── interaction.py
├── main.py
├── motion.py
├── tracker.py
├── utils.py
└── video_io.py
```

---

## Installation

```bash
git clone https://github.com/abenmabrouk/violence-detection-yolo.git

cd violence-detection-yolo

python -m venv .venv

# Linux
source .venv/bin/activate

# Windows
.venv\Scripts\activate

pip install -r requirements.txt
```

---

## Technologies

- Python
- OpenCV
- Ultralytics YOLOv8
- ByteTrack
- NumPy

---

## Roadmap

- [x] Person Detection
- [x] Multi-object Tracking
- [x] Motion Analysis
- [x] Interaction Analysis
- [ ] Behavior Analysis
- [ ] Event Detection
- [ ] Violence Classification

---

## Author

**Amira Ben Mabrouk**

PhD in Information Technology

Computer Vision • Deep Learning • Video Surveillance • Artificial Intelligence