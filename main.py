```python
import cv2
import mediapipe as mp


def blur_face(frame, x, y, width, height):
    """Blur a detected face region."""
    frame_height, frame_width = frame.shape[:2]

    # Convert the bounding box to valid image coordinates
    x1 = max(0, x)
    y1 = max(0, y)
    x2 = min(frame_width, x + width)
    y2 = min(frame_height, y + height)

    if x1 >= x2 or y1 >= y2:
        return frame

    face = frame[y1:y2, x1:x2]

    # Apply strong blur to hide facial features
    blurred_face = cv2.GaussianBlur(face, (51, 51), 0)

    frame[y1:y2, x1:x2] = blurred_face

    return frame


def main():
    # Open the default webcam
    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        print("ERROR: Unable to access the webcam.")
        return

    # Initialize MediaPipe Face Detection
    mp_face_detection = mp.solutions.face_detection

    with mp_face_detection.FaceDetection(
        model_selection=0,
        min_detection_confidence=0.5
    ) as detector:

        print("Real-Time Face Anonymizer")
        print("-------------------------")
        print("Webcam started successfully.")
        print("Press 'q' to exit.")

        while True:
            success, frame = camera.read()

            if not success:
                print("ERROR: Unable to read webcam frame.")
                break

            # Convert BGR image to RGB for MediaPipe
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Detect faces
            results = detector.process(rgb_frame)

            if results.detections:
                for detection in results.detections:

                    bounding_box = (
                        detection.location_data.relative_bounding_box
                    )

                    frame_height, frame_width = frame.shape[:2]

                    x = int(bounding_box.xmin * frame_width)
                    y = int(bounding_box.ymin * frame_height)

                    width = int(bounding_box.width * frame_width)
                    height = int(bounding_box.height * frame_height)

                    # Anonymize the detected face
                    frame = blur_face(
                        frame,
                        x,
                        y,
                        width,
                        height
                    )

            # Display the anonymized video
            cv2.imshow(
                "Real-Time Face Anonymizer",
                frame
            )

            # Press q to quit
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

    camera.release()
    cv2.destroyAllWindows()

    print("Application closed.")


if __name__ == "__main__":
    main()
```

