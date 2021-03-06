from time import sleep,strftime,localtime

from gpiozero import MotionSensor
from camera import Camera
from led import Led
from client import ClientHTTP


class NatureCam:

    def __init__(self, lights=False):
        self.pir = MotionSensor(27)
        if lights:
            self.red = Led(4)
            self.green = Led(17)
        print('Starting camera.')
        self.camera = Camera(resolution=(640, 480))
        self.pir.when_motion = self._recording
        self.pir.when_no_motion = self._standby
        #self.green.turn_on()

    def _standby(self):
        print("3 standby")
        if hasattr(self, 'red'):
            self.green.turn_on()
            self.red.turn_off()

    def _recording(self):
        print("2 recording")
        self.camera.capture()
        self.camera.record(strftime("%A-%d-%B-%Y_%H_%M_%S", localtime()))
        sleep(2)

    def activate(self):
        if hasattr(self, 'red'):
            self.red.turn_on()

        self.start_streaming()
        if hasattr(self, 'red'):
            self.red.turn_off()

        #pause()
        #while True:
        #    print("1 Waiting for motion")
        #    self.pir.wait_for_motion()
        #    sleep(8)

    def start_recording(self):
        sleep(3)
        self.camera.record(strftime("%A-%d-%B-%Y_%H_%M_%S", localtime()), 60, True)

    def start_streaming(self):
        client_socket = ClientHTTP()
        connection = client_socket.start('192.168.0.141')
        self.camera.stream(connection, client_socket)




