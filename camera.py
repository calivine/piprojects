from time import sleep, localtime, strftime

from picamera import PiCamera


class Camera:

    def __init__(self, resolution=(1024, 768), framerate=24):
        self.camera = PiCamera(resolution=resolution)
        self.camera.rotation = 180

    def capture(self):
        self.camera.capture(strftime("%A-%d-%B-%Y_%H_%M_%S.jpg", localtime()))

    def capture_timelapse(self, time=300):
        for filename in self.camera.capture_continuous('image{timestamp:%H-%M-%S-%f}.jpg'):
            print('Captured %s' % filename)
            # wait time defaults to 5 minutes
            sleep(time)

    def record(self, output, duration=5, streaming=False):
        self.camera.start_recording("{}.h264".format(output), format='h264')
        self.camera.wait_recording(duration)
        self.camera.stop_recording()







