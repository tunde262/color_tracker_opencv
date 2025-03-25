# Detect & Track Colors using Computer Vision

This project demonstrates real-time color detection and tracking using Python and OpenCV. It captures live webcam footage, converts it from RGB to HSV, and applies a masking function to detect a specified color range. The program then draws a bounding box around the detected color in real-time.

![thumbnail](https://github.com/tunde262/color_tracker_opencv/blob/main/assets/thumbnail.png?raw=true)

## Project Goal

The goal of this project was to explore the applications of computer vision in color detection by building an app that processes video footage to identify and track objects based on their color.

## Features
- Real-time color detection and tracking using a webcam feed.
- Converts RGB video frames to HSV for accurate color detection.
- Uses a masking function to isolate specific color ranges.
- Draws a bounding box around the detected color.
- Runs efficiently with simple keypress exit functionality.

## Code Explanation
- The program starts by loading the webcam feed using `cv2.VideoCapture(0)`. Each frame is processed in a loop until the user presses the 'q' key to exit.
- The video frames are converted from RGB to HSV format using `cv2.cvtColor()`.
- A masking function isolates the target color based on defined HSV thresholds.
- The `PIL.Image.fromarray()` function converts the mask to a format that allows extracting the bounding box coordinates of the detected color.
- The bounding box is drawn around the detected color using OpenCV's `cv2.rectangle()` function.

## Requirements
- Python 3.x
- OpenCV (`opencv-python` package)
- NumPy (`numpy` package)
- Pillow (`pillow` package)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/tunde262/color_tracker_opencv.git
   cd color_tracker_opencv

2. Install the necessary dependencies:

   ```bash
   pip install opencv-python numpy pillow

## How To Run

1. Make sure your webcam is connected and functional.

2. Run the Python script to start the program:
   
   ```bash
   python main.py

3. The webcam feed will appear with boxes tracking the specified color. Press the `q` key to exit the program.
