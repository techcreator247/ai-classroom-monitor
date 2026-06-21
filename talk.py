import cv2
import numpy as np

def detect_talking(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    laplacian = cv2.Laplacian(gray, cv2.CV_64F).var()

    # motion-based heuristic
    return laplacian > 120