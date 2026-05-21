# Real-Time Face Anonymizer

A real-time face anonymization project using OpenCV and MediaPipe.

The program detects faces from a webcam feed and applies blur to anonymize them in real time.

## Features

- Real-time webcam face detection
- Automatic face anonymization
- Blur effect on detected faces
- MediaPipe face detection integration

## Technologies Used

- Python
- OpenCV
- MediaPipe

## Installation

```bash
pip install -r requirements.txt
```

## Run

```bash
python main.py
```

## How It Works

1. Captures webcam frames
2. Detects faces using MediaPipe
3. Extracts face region
4. Applies blur effect
5. Displays anonymized video feed

## Future Improvements

- Mosaic pixel anonymization
- Video file anonymization
- Face tracking
- Detection confidence display
- Save processed video

## Author

Hrisheekesh S