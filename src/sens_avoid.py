import RPi.GPIO as gpio
import time
import random

gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)
gpio.setup(7, gpio.OUT)
gpio.setup(11, gpio.OUT)
gpio.setup(13, gpio.OUT)
gpio.setup(15, gpio.OUT)

# TODO: Create seperate file with direction functions and import functions
#       from there.


def forward():
    gpio.output(7, True)
    gpio.output(11, False)
    gpio.output(13, False)
    gpio.output(15, True)


def turn_right(tf):
    gpio.output(7, True)
    gpio.output(11, False)
    gpio.output(13, False)
    gpio.output(15, False)
    time.sleep(tf)


def turn_left(tf):
    gpio.output(7, False)
    gpio.output(11, False)
    gpio.output(13, False)
    gpio.output(15, True)
    time.sleep(tf)


def reverse(tf):
    gpio.output(7, False)
    gpio.output(11, True)
    gpio.output(13, True)
    gpio.output(15, False)
    time.sleep(tf)

def stop(tf):
    gpio.output(7, False)
    gpio.output(11, False)
    gpio.output(13, False)
    gpio.output(15, False)
    time.sleep(tf)


def distanceLeft():
    TRIG = 18
    ECHO = 12

    gpio.setmode(gpio.BOARD)
    gpio.setwarnings(False)

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

    return distance


def distanceAhead():
    TRIG_2 = 40
    ECHO_2 = 38

    gpio.setmode(gpio.BOARD)
    gpio.setwarnings(False)

    gpio.setup(TRIG_2, gpio.OUT)
    gpio.setup(ECHO_2, gpio.IN)

    gpio.output(TRIG_2, True)
    time.sleep(0.0001)
    gpio.output(TRIG_2, False)

    while gpio.input(ECHO_2) == 0:
        start = time.time()

    while gpio.input(ECHO_2) == 1:
        end = time.time()

    sig_time = end - start

    distance = sig_time / 0.000058

    return distance


def distRight():
    gpio.setmode(gpio.BOARD)
    gpio.setwarnings(False)

    TRIG_3 = 37
    ECHO_3 = 35

    gpio.setup(TRIG_3, gpio.OUT)
    gpio.setup(ECHO_3, gpio.IN)

    gpio.output(TRIG_3, True)
    time.sleep(0.0001)
    gpio.output(TRIG_3, False)

    while gpio.input(ECHO_3) == 0:
        start = time.time()

    while gpio.input(ECHO_3) == 1:
        end = time.time()

    sig_time = end - start

    distance = sig_time / 0.000058

    return distance


try:	
    while True:
        dist_ahead = distanceAhead()
        dist_left = distanceLeft()
        dist_right = distRight()
        stop_dist = 7
        stop_time = 1
        move_time = 2

        if dist_ahead < stop_dist:
            print('Redirecting...')
            stop(stop_time)
            print('Finding best route...')
            reverse(move_time)
            if dist_left < dist_right:
                print('Turning right...')
                turn_right(move_time)
            elif dist_right < dist_left:
                print('Turning left...')
                turn_left(move_time)
        elif dist_left < stop_dist:
            print('Redirecting...')
            stop(stop_time)
            print('Redirecting...')
            reverse(move_time)
            print('Turning right...')
            turn_right(move_time)
        elif dist_right < stop_dist:
            print('Redirecting...')
            stop(stop_time)
            print('Redirecting...')
            reverse(move_time)
            print('Turning left...')
            turn_left(move_time)
        else:
            forward()
            print 'Left: {} cm |'.format(dist_left), 'Ahead: {} cm |'.format(dist_ahead), 'Right: {} cm'.format(dist_right)

finally:
    if KeyboardInterrupt:
        gpio.cleanup()
