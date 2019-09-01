import RPi.GPIO as gpio 
import time

gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)

TRIG = 18
ECHO = 12  

gpio.setup(TRIG, gpio.OUT)
gpio.setup(ECHO, gpio.IN)

gpio.output(TRIG, True)
time.sleep(0.0001)
gpio.output(TRIG, False)

while gpio.input(ECHO) == 0:
    start = time.time()

while gpio.input(ECHO) == 1:
    end = time.time()

sig_time = end - start

distance = sig_time / 0.000058

print('Distance: {} cm'.format(distance))

gpio.cleanup()
