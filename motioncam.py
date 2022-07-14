import sys
from time import sleep

from gpiozero import MotionSensor
from camera import Camera
from led import Led

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
    try:
        print("1 Waiting for motion")
        pir.wait_for_motion()
        sleep(3)
    finally:
        print("Closing")
        camera.camera.close()
        if red.light.is_lit():
            red.turn_off()
        elif green.light.is_lit():
            green.turn_off()



    # camera.capture(strftime("%A-%d-%B-%Y_%X.jpg", localtime()))
