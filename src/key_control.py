import curses
import RPi.GPIO as gpio

gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)
gpio.setup(7, gpio.OUT)
gpio.setup(11, gpio.OUT)
gpio.setup(13, gpio.OUT)
gpio.setup(15, gpio.OUT)

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

# TODO: Create seperate file with direction functions and import functions
#       from there.


def forward():
    gpio.output(7, True)
    gpio.output(11, False)
    gpio.output(13, False)
    gpio.output(15, True)


def reverse():
    gpio.output(7, False)
    gpio.output(11, True)
    gpio.output(13, True)
    gpio.output(15, False)


def turn_right():
    gpio.output(7, True)
    gpio.output(11, False)
    gpio.output(13, False)
    gpio.output(15, False)


def turn_left():
    gpio.output(7, False)
    gpio.output(11, False)
    gpio.output(13, False)
    gpio.output(15, True)


def pivot_right():
    gpio.output(7, True)
    gpio.output(11, False)
    gpio.output(13, True)
    gpio.output(15, False)


def pivot_left():
    gpio.output(7, False)
    gpio.output(11, True)
    gpio.output(13, False)
    gpio.output(15, True)


def stop():
    gpio.output(7, False)
    gpio.output(11, False)
    gpio.output(13, False)
    gpio.output(15, False)


try:
    while True:
        char = screen.getch()
        if char == ord('x'):
            break
        elif char == curses.KEY_UP:
            forward()
        elif char == ord('w'):
            forward()
        elif char == curses.KEY_DOWN:
            reverse()
        elif char == ord('s'):
            reverse()
        elif char == curses.KEY_RIGHT:
            turn_right()
        elif char == ord('d'):
            turn_right()
        elif char == curses.KEY_LEFT:
            turn_left()
        elif char == ord('a'):
            turn_left()
        elif char == ord('e'):
            pivot_right()
        elif char == ord('q'):
            pivot_left()
        elif char == 10:
            stop()
        elif char == ord(' '):
            stop()

finally:
    curses.nocbreak()
    screen.keypad(0)
    curses.echo()
    curses.endwin()
    gpio.cleanup()
