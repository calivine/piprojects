from signal import pause
from time import sleep,strftime,localtime

from gpiozero import MotionSensor
from camera import Camera
from led import Led


class NatureCam:

    def __init__(self):
        self.pir = MotionSensor(27)
        self.red = Led(4)
        self.green = Led(17)
        self.camera = Camera(resolution=(640, 480))
        self.pir.when_motion = self._recording
        self.pir.when_no_motion = self._standby
        self.green.turn_on()

    def _standby(self):
        print("3 standby")
        self.green.turn_on()
        self.red.turn_off()

    def _recording(self):
        print("2 recording")
        self.green.turn_off()
        self.red.turn_on()
        self.camera.capture()
        self.camera.record(strftime("%A-%d-%B-%Y_%H_%M_%S", localtime()))
        sleep(2)

    def activate(self):
        pause()
        #while True:
        #    print("1 Waiting for motion")
        #    self.pir.wait_for_motion()
        #    sleep(8)

    def start_streaming(self):
        sleep(3)
        self.camera.record(strftime("%A-%d-%B-%Y_%H_%M_%S", localtime()), 60, True)

