def main():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not access the webcam.")
        return

    mp_face_detection = mp.solutions.face_detection

    with mp_face_detection.FaceDetection(
        model_selection=0,
        min_detection_confidence=0.5
    ) as face_detection:

        print("Real-Time Face Anonymizer started.")
        print("Press 'q' to quit.")

        while True:
            ret, img = cap.read()

            if not ret:
                print("Error: Could not read a frame from the webcam.")
                break

            img = process(img, face_detection)

            cv2.imshow("Real-Time Face Anonymizer", img)

            if cv2.waitKey(40) & 0xFF == ord("q"):
                break

    cap.release()
    cv2.destroyAllWindows()
    print("Face anonymizer stopped.")
