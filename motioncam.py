import sys
from time import sleep, localtime, strftime
from picamera import PiCamera
from gpiozero import MotionSensor
from camera import Camera
from led import Led

pir = MotionSensor(27)
red = Led(4)
green = Led(17)

#camera = PiCamera(resolution=(1024, 768))

#camera.rotation = 180

camera = Camera()

def standby():
    green.turn_on()
    red.turn_off()


def recording():
    green.turn_off()
    red.turn_on()
    camera.capture()
    sleep(2)

pir.when_motion = recording

pir.when_no_motion = standby

while True:
    try:
        pir.wait_for_motion()
    except KeyboardInterrupt:
        camera.camera.close()
        sys.exit()

    # print("Motion detected!")

    # camera.capture(strftime("%A-%d-%B-%Y_%X.jpg", localtime()))
