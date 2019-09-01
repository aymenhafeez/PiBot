import RPi.GPIO as gpio
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np
import math

gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)
gpio.setup(7, gpio.OUT)
gpio.setup(11, gpio.OUT)
gpio.setup(13, gpio.OUT)
gpio.setup(15, gpio.OUT)

theta = 0
max_line_gap = 7.5
min_line_length = 2.5

camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 30
rawCapture = PiRGBArray(camera, size=(640, 480))
time.sleep(0.1)

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    image = frame.array
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(blurred, 50, 50)
    lines = cv2.HoughLinesP(edged, 1, np.pi / 180, 10,
                            maxLineGap=max_line_gap,
                            minLineLength=min_line_length)
    if lines.all() is not None:
        for x in range(0, len(lines)):
            for x1, y1, x2, y2 in lines[x]:
                cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
                theta = theta + math.atan2((y2 - y1), (x2 - x1))

    threshold = 6

    if(theta > threshold):
        gpio.output(7, True)
        gpio.output(11, False)
        gpio.output(13, True)
        gpio.output(15, False)
        print('left')

    if(theta < -threshold):
        gpio.output(7, False)
        gpio.output(11, True)
        gpio.output(13, False)
        gpio.output(15, True)
        print('right')

    if(abs(theta) < threshold):
        gpio.output(7, True)
        gpio.output(11, False)
        gpio.output(13, False)
        gpio.output(15, True)
        print('straight')

    theta = 0
    print(lines)

    cv2.imshow("Frame", image)
    key = cv2.waitKey(1) & 0xFF
    rawCapture.truncate(0)
    if key == ord('x'):
        gpio.cleanup()
        break
