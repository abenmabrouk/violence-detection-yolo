import config
import utils

def detect_persons(result, model):
    """
    Extract detected persons from a YOLO result.

    Parameters
    ----------
    result : ultralytics.engine.results.Results

    Returns
    -------
    list
        List of detected persons.
    """
    persons = []

    for box in result.boxes:

        # classe détectée

        class_id = int(box.cls[0])

        if class_id != config.PERSON_CLASS:
            continue

        # confiance
        confidence = float(box.conf[0])

        track_id = None

        if confidence < config.CONFIDENCE_THRESHOLD:
            continue
        # coordonnées
        x1, y1, x2, y2 = box.xyxy[0]

        bbox = (
            int(x1),
            int(y1),
            int(x2),
            int(y2)
        )

        center = utils.get_center(bbox)


        if box.id is not None:
            track_id = int(box.id.item())      
        

        persons.append({
            "id": track_id,
            "class_name": model.names[class_id],
            "confidence": confidence,
            "bbox": (
                int(x1),
                int(y1),
                int(x2),
                int(y2)
            ),
            "center": center
            })
    return persons