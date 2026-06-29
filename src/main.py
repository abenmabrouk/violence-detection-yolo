from ultralytics import YOLO
import config
import detector
import drawing
import video_io
import tracker

def main():
    model = YOLO(config.MODEL_PATH)

    cap = video_io.open_video(config.VIDEO_PATH)

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

        persons = detector.detect_persons(result,model)

        tracker.update_tracks(persons, tracks)

        drawing.draw_persons(frame, persons)

        drawing.draw_tracks(frame, tracks)

        drawing.draw_motion(frame, persons, tracks)

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