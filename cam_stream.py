import cv2
import numpy as np


cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('Frame', frame)

    key = cv2.waitKey(1)

    if key == 10:
        break

cap.release()
cv2.destroyAllWindows()
