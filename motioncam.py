from time import sleep, localtime, strftime
from picamera import PiCamera
from gpiozero import MotionSensor
from camera import Camera

pir = MotionSensor(4)

#camera = PiCamera(resolution=(1024, 768))

#camera.rotation = 180

camera = Camera()

pir.when_motion = camera.capture()


while True:
    pir.wait_for_motion()

    # print("Motion detected!")

    # camera.capture(strftime("%A-%d-%B-%Y_%X.jpg", localtime()))
