'''Testing the ultrasonic distance sensor'''

import RPi.GPIO as gpio 
import time

gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)

# Setting the TRIG and ECHO pins as variables to the corresponding GPIO pins.
TRIG = 18
ECHO = 12  

gpio.setup(TRIG, gpio.OUT)
gpio.setup(ECHO, gpio.IN)

gpio.output(TRIG, True)
time.sleep(0.0001)
gpio.output(TRIG, False)

while gpio.input(ECHO) == False:
    sig_start = time.time()

while gpio.input(ECHO) == True:
    sig_end = time.time()

sig_time = sig_end - sig_start

distance = sig_time / 0.000058

print('Distance: {} cm'.format(distance))

gpio.cleanup()
