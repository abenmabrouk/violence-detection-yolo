import cv2
from ultralytics import YOLO
import config
import detector
import drawing
import interaction
import video_io
import tracker
import motion

def main():
    model = YOLO(config.MODEL_PATH)

    cap = video_io.open_video(config.VIDEO_PATH)
    fps = cap.get(cv2.CAP_PROP_FPS)

    writer = video_io.create_writer(config.output_video,cap)

    tracks = {}

    frame_number = 0

    while cap.isOpened():

        ret, frame = cap.read()

        if not ret:
            break

        frame_number += 1

        results = model.track(
            frame,
            persist=True,
            tracker="bytetrack.yaml",
            verbose=False
        )

        result = results[0]

        # Détection
        persons = detector.detect_persons(result, model)

        # Mise à jour des trajectoires
        tracker.update_tracks(persons, tracks)

        # Calcul du mouvement
        for person in persons:

            track_id = person["id"]

            if track_id is None:
                continue

            if track_id not in tracks:
                continue

            person["motion"] = motion.compute_motion(
                tracks[track_id],
                fps
            )

        # Interactions
        interactions = interaction.compute_pairwise_distances(persons)

        contacts = interaction.detect_close_contacts(interactions)

        density = interaction.compute_local_density(
            persons,
            radius=150
        )

        for person in persons:

            track_id = person["id"]

            if track_id in density:
                person["density"] = density[track_id]

        # Dessin
        drawing.draw_persons(frame, persons)

        drawing.draw_tracks(frame, tracks)

        drawing.draw_motion(frame, persons)

        drawing.draw_interactions(frame, persons, contacts)

        writer.write(frame)

        if frame_number % 30 == 0:

            print(
                f"Frame {frame_number} | "
                f"Persons: {len(persons)} | "
                f"Tracks: {len(tracks)}"
            )

    cap.release()
    writer.release()

if __name__ == "__main__":
    main()