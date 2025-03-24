# Find Color Limits for Object Detection
import numpy as np
import cv2

def get_limits(color):

    # Convert input BGR color into NumPy array
    c = np.uint8([[color]])

    # Convert BGR NumPy array to HSV color space
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    # Define lower & upper HSV limits
    lowerLimit = hsvC[0][0][0] - 10, 100, 100
    upperLimit = hsvC[0][0][0] + 10 , 255, 255

    # Convert limits to NumPy arrays of type uint8
    lowerLimit = np.array(lowerLimit, dtype=np.uint8)
    upperLimit = np.array(upperLimit, dtype=np.uint8)

    # Return color range (lower, upper) 
    return lowerLimit, upperLimit