# Real-Time Face Anonymizer

A Python-based computer vision project that detects human faces from a live webcam feed and anonymizes them in real time using blur.

The project uses **OpenCV** for video capture and image processing and **MediaPipe Face Detection** for detecting faces.

## Features

* Real-time face detection from a webcam
* Automatic anonymization of detected faces
* Blur-based face anonymization
* Multiple faces can be detected in the same frame
* Runs directly from the command line
* No external API or internet connection is required during execution

## Technologies Used

* Python
* OpenCV
* MediaPipe

## Project Structure

```text
realtime-face-anonymizer/
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Requirements

Before running the project, make sure the following are installed:

* Python 3.9 or later
* A working webcam
* Internet connection for the initial installation of Python packages

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Hrishi920/realtime-face-anonymizer.git
```

Move into the project directory:

```bash
cd realtime-face-anonymizer
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

## Running the Project

Run the following command from the project directory:

```bash
python main.py
```

The program will attempt to access the default webcam.

A window named **Real-Time Face Anonymizer** will open and display the webcam feed.

Detected faces will automatically be blurred.

Press:

```text
q
```

to stop the program.

## How It Works

The project follows these steps:

1. OpenCV accesses the computer's webcam.
2. Each webcam frame is captured as an image.
3. The frame is converted from BGR to RGB format.
4. MediaPipe Face Detection processes the frame and identifies faces.
5. The relative bounding box of each detected face is converted into pixel coordinates.
6. The detected face region is extracted from the frame.
7. OpenCV blur is applied to the face region.
8. The processed frame is displayed in real time.
9. The process continues until the user presses `q`.

## Configuration

The project uses the default webcam:

```python
cv2.VideoCapture(0)
```

The value `0` represents the default camera.

If the computer has multiple cameras, this value can be changed to another camera index such as `1`.

The face detection confidence threshold is set to:

```python
min_detection_confidence=0.5
```

A higher value can be used when more conservative face detection is required.

## Troubleshooting

### Webcam cannot be accessed

If the terminal displays:

```text
Error: Could not access the webcam.
```

check that:

* The webcam is connected.
* No other application is currently using the webcam.
* Camera permissions are enabled for Python.
* The correct camera index is being used.

### Packages are not installed

Run:

```bash
pip install -r requirements.txt
```

If a virtual environment is being used, make sure it is activated before installing the dependencies.

## Privacy

The project processes the webcam frames locally on the computer.

No images or video frames are uploaded to an external server or cloud service.

## Future Improvements

Possible future extensions include:

* Pixelation/mosaic-based anonymization
* Video file anonymization
* Face tracking
* Configurable blur intensity
* Saving anonymized video
* Displaying face detection confidence
* Support for different input sources

## Author

**Hrisheekesh S**


Hrisheekesh S
