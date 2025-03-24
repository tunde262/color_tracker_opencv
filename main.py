# Color Detection with Python | OpenCV + Webcam
import cv2
from PIL import Image # PIL library for handling images 
from util import get_limits

# Load Webcam Video
webcam = cv2.VideoCapture(0)

# Define target color in BGR color space
yellow = [0, 255, 255]

while True:

    # Capture the frame from webcam
    successful_frame_read, frame = webcam.read()

    # Convert frame from BGR -> HSV color space
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Get lower & upper HSV range for detecting color
    lowerLimit, upperLimit = get_limits(color=yellow)

    # Apply color detection algorithm
    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

    # Convert mask to PIL image for box detection
    mask_ = Image.fromarray(mask)

    # Get box coordinates for color region
    bounding_box = mask_.getbbox()

    # Draw box around object if detected 
    if bounding_box is not None:
        x1, y1, x2, y2 = bounding_box

        # Green box
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 5)

    # Load window onto screen
    cv2.imshow('frame', frame)

    # Hit 'q' key to quit program
    if cv2.waitKey(1) & 0XFF == ord('q'):
        break

# Close window
webcam.release()
cv2.destroyAllWindows()