import cv2
from pathlib import Path

# Chemins
VIDEO_PATH = Path("data/videos/test1.mp4")
OUTPUT_DIR = Path("results/videos")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
output_video = OUTPUT_DIR / VIDEO_PATH.name
MODEL_PATH = Path("models/yolov8n.pt")

# Classes
PERSON_CLASS = 0

# Détection
CONFIDENCE_THRESHOLD = 0.50

# Dessin
BOX_COLOR = (0, 255, 0)
TRACK_COLOR = (255, 0, 0)
CENTER_COLOR = (0, 0, 255)
CENTER_RADIUS = 5

BOX_THICKNESS = 2
FONT_SCALE = 0.6
FONT = cv2.FONT_HERSHEY_SIMPLEX

ARROW_COLOR = (255,0,255)
ARROW_LENGTH = 40
ARROW_THICKNESS = 2