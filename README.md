# Violence Detection using YOLOv8

## Description

This project aims to build a complete computer vision pipeline for violence detection in surveillance videos.

Current features:

- Person detection using YOLOv8
- Multi-object tracking using ByteTrack
- Trajectory visualization
- Motion analysis
- Speed estimation
- Direction estimation

Future work:

- Interaction analysis
- Violence feature extraction
- Violence classification


## Installation

```bash
git clone https://github.com/abenmabrouk/violence-detection-yolo.git

cd violence-detection-yolo

python -m venv .venv

source .venv/bin/activate
# Windows
.venv\Scripts\activate

pip install -r requirements.txt
```