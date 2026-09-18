import cv2
import mediapipe as mp


def process(img, face_detection):
    height, width, _ = img.shape

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = face_detection.process(img_rgb)

    if results.detections:
        for detection in results.detections:
            bbox = detection.location_data.relative_bounding_box

            x1 = int(bbox.xmin * width)
            y1 = int(bbox.ymin * height)
            x2 = int((bbox.xmin + bbox.width) * width)
            y2 = int((bbox.ymin + bbox.height) * height)

            # Keep bounding box inside the image
            x1 = max(0, x1)
            y1 = max(0, y1)
            x2 = min(width, x2)
            y2 = min(height, y2)

            # Apply blur only if the bounding box is valid
            if x2 > x1 and y2 > y1:
                face_region = img[y1:y2, x1:x2]
                img[y1:y2, x1:x2] = cv2.blur(face_region, (50, 50))

    return img


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


if __name__ == "__main__":
    main()
