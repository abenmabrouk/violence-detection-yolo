import cv2
import config
import utils

import cv2
import config


def draw_persons(frame, persons):

    """
    Draw bounding boxes, labels and centers.
    """

    for person in persons:

        x1, y1, x2, y2 = person["bbox"]
        cx, cy = person["center"]

        label = person["class_name"]

        if person["id"] is not None:
            label += f" #{person['id']}"

        # Bounding box
        cv2.rectangle(
            frame,
            (x1, y1),
            (x2, y2),
            config.BOX_COLOR,
            config.BOX_THICKNESS
        )

        # Label
        cv2.putText(
            frame,
            label,
            (x1, y1 - 10),
            config.FONT,
            config.FONT_SCALE,
            config.BOX_COLOR,
            config.BOX_THICKNESS
        )

        # Center
        cv2.circle(
            frame,
            (cx, cy),
            config.CENTER_RADIUS,
            config.CENTER_COLOR,
            -1
        )

import cv2
import config
import utils


def draw_motion(frame, persons, tracks):

    """
    Draw speed and motion direction.
    """

    for person in persons:

        track_id = person["id"]

        if track_id is None:
            continue

        if track_id not in tracks:
            continue

        points = tracks[track_id]

        speed = utils.compute_speed(points)

        direction = utils.compute_direction(points)

        cx, cy = person["center"]

        dx, dy = direction

        end_point = (
            int(cx + dx * config.ARROW_LENGTH),
            int(cy + dy * config.ARROW_LENGTH)
        )

        # Arrow
        cv2.arrowedLine(
            frame,
            (cx, cy),
            end_point,
            config.ARROW_COLOR,
            config.ARROW_THICKNESS,
            tipLength=0.3
        )
        label = f"ID:{track_id}  V:{speed:.1f}"

        # Speed
        cv2.putText(
            frame,
            label,
            (cx + 10, cy + 20),
            config.FONT,
            0.5,
            config.ARROW_COLOR,
            2
        )
        
def draw_tracks(frame, tracks):

    for points in tracks.values():

        if len(points) < 2:
            continue

        for i in range(1, len(points)):

            cv2.line(
                frame,
                points[i-1],
                points[i],
                config.TRACK_COLOR,
                2
            )
