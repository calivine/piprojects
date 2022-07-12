from time import sleep, localtime, strftime
from picamera import PiCamera
from gpiozero import MotionSensor

pir = MotionSensor(4)


camera = PiCamera(resolution=(1024, 768))

camera.rotation = 180

while True:
    pir.wait_for_motion()

    print("Motion detected!")

    camera.capture(strftime("%A-%d-%B-%Y_%X.jpg", localtime()))
