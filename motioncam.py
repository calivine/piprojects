import sys
from time import sleep, localtime, strftime
import signal

from picamera import PiCamera
from gpiozero import MotionSensor
from camera import Camera
from led import Led


def sigint_handler(signal, frame):
    print('KeyboardInterrupt is caught')
    camera.camera.close()
    if red.light.is_lit():
        red.turn_off()
    elif green.light.is_lit():
        green.turn_off()
    sys.exit()


signal.signal(signal.SIGINT, sigint_handler)

# Pins being used
pir = MotionSensor(27)
red = Led(4)
green = Led(17)


camera = Camera()


def standby():
    print("3 standby")
    green.turn_on()
    red.turn_off()


def recording():
    print("2 recording")
    green.turn_off()
    red.turn_on()
    camera.capture()
    sleep(2)


pir.when_motion = recording

pir.when_no_motion = standby

while True:
    print("1 Waiting for motion")
    pir.wait_for_motion()
    print("4 Motion detected!")
    sleep(2)


    # camera.capture(strftime("%A-%d-%B-%Y_%X.jpg", localtime()))
