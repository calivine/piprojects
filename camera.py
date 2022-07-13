from time import sleep, localtime, strftime

from picamera import PiCamera

class Camera:

    def __init__(self):
        self.camera = PiCamera(resolution=(1024, 768))
        self.camera.rotation = 180

    def capture(self):
        self.camera.capture(strftime("%A-%d-%B-%Y_%H_%M_%S.jpg", localtime()))

