import cv2
import config
import utils


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

        if "motion" in person:
            speed = person["motion"]["speed"]
            label += f' | {speed:.1f}px/s'

        if "density" in person:
            label += f' | D:{person["density"]}'

        risk = person["behavior"]["risk_level"]
        if risk == "HIGH":
            color = (255, 0, 0)

        elif risk == "MEDIUM":
            color = (255, 100, 0)

        else:
            color = (0, 255, 0)
            
        label += f' | {risk}'

        # Bounding box
        cv2.rectangle(
            frame,
            (x1, y1),
            (x2, y2),
            color,
            config.BOX_THICKNESS
        )

        # Label
        cv2.putText(
            frame,
            label,
            (x1, y1 - 10),
            config.FONT,
            config.FONT_SCALE,
            color,
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

def draw_motion(frame, persons):
    """
    Draw motion information (speed, direction and angle).
    """

    for person in persons:

        if "motion" not in person:
            continue

        cx, cy = person["center"]

        motion = person["motion"]

        speed = motion["speed"]
        direction = motion["direction"]
        angle = motion["angle"]

        dx, dy = direction

        end_point = (
            int(cx + dx * config.ARROW_LENGTH),
            int(cy + dy * config.ARROW_LENGTH)
        )

        # Draw motion arrow
        cv2.arrowedLine(
            frame,
            (cx, cy),
            end_point,
            config.ARROW_COLOR,
            config.ARROW_THICKNESS,
            tipLength=0.3
        )

        # Speed
        cv2.putText(
            frame,
            f"V:{speed:.1f}",
            (cx + 10, cy + 20),
            config.FONT,
            0.5,
            config.ARROW_COLOR,
            2
        )

        # Direction angle
        cv2.putText(
            frame,
            f"{angle:.0f}°",
            (cx + 10, cy + 40),
            config.FONT,
            0.5,
            (255, 255, 0),
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

def draw_interactions(frame, persons, contacts):

    centers = {}

    for person in persons:

        centers[person["id"]] = person["center"]

    for contact in contacts:

        id1 = contact["person1"]
        id2 = contact["person2"]

        if id1 not in centers:
            continue

        if id2 not in centers:
            continue

        p1 = centers[id1]
        p2 = centers[id2]

        distance = contact["distance"]

        color = (0,255,0)

        if distance < 60:
            color = (0,0,255)

        elif distance < 120:
            color = (0,165,255)

        cv2.line(
            frame,
            p1,
            p2,
            color,
            2
        )

        mx = (p1[0] + p2[0]) // 2
        my = (p1[1] + p2[1]) // 2

        cv2.putText(
            frame,
            f"{distance:.0f}",
            (mx, my),
            config.FONT,
            0.5,
            color,
            2
        )
