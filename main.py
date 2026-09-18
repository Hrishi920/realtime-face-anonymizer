import cv2
import mediapipe as mp


def anonymize_faces(frame, detector):
    height, width = frame.shape[:2]

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = detector.process(rgb_frame)

    if results.detections:
        for detection in results.detections:
            box = detection.location_data.relative_bounding_box

            x1 = max(0, int(box.xmin * width))
            y1 = max(0, int(box.ymin * height))

            x2 = min(
                width,
                int((box.xmin + box.width) * width)
            )

            y2 = min(
                height,
                int((box.ymin + box.height) * height)
            )

            if x2 > x1 and y2 > y1:
                face = frame[y1:y2, x1:x2]

                frame[y1:y2, x1:x2] = cv2.GaussianBlur(
                    face,
                    (51, 51),
                    0
                )

    return frame


def main():
    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        print("Error: Could not access the webcam.")
        return

    mp_face_detection = mp.solutions.face_detection

    with mp_face_detection.FaceDetection(
        model_selection=0,
        min_detection_confidence=0.5
    ) as detector:

        print("Real-Time Face Anonymizer Started")
        print("Press Q to exit")

        while True:
            success, frame = camera.read()

            if not success:
                print("Error: Could not read webcam frame.")
                break

            frame = anonymize_faces(frame, detector)

            cv2.imshow(
                "Real-Time Face Anonymizer",
                frame
            )

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

    camera.release()
    cv2.destroyAllWindows()

    print("Application closed.")


if __name__ == "__main__":
    main()
