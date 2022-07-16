import sys
from time import sleep,strftime,localtime

from gpiozero import MotionSensor
from camera import Camera
from led import Led

# Pins being used
pir = MotionSensor(27)
red = Led(4)
green = Led(17)
camera = Camera(resolution=(640, 480))


def standby():
    print("3 standby")
    green.turn_on()
    red.turn_off()


def recording():
    print("2 recording")
    green.turn_off()
    red.turn_on()
    camera.capture()
    camera.record(strftime("%A-%d-%B-%Y_%H_%M_%S", localtime()))
    sleep(2)


pir.when_motion = recording

pir.when_no_motion = standby

green.turn_on()

while True:
    print("1 Waiting for motion")
    pir.wait_for_motion()
    sleep(8)



    # camera.capture(strftime("%A-%d-%B-%Y_%X.jpg", localtime()))
