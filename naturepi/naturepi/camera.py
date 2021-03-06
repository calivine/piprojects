from time import sleep, localtime, strftime
import datetime as dt
import subprocess

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
        #self.camera.framerate = 24
        #self.camera.resolution = (640, 480)
        # sleep(1)
        self.camera.annotate_text = self._timestamp()
        self.camera.start_recording("{}.h264".format(output), splitter_port=2, format='h264')
        self.camera.wait_recording(10)
        if streaming:
            self.camera.start_recording("{}_stream.h264".format(output), splitter_port=2, format='h264')
        self.camera.wait_recording(duration)
        if streaming:
            self.camera.stop_recording(splitter_port=2)
        self.camera.stop_recording(splitter_port=2)
        # FFmpeg to convert video to .mkv
        subprocess.Popen(['ffmpeg', '-i', '{}.h264'.format(output), '{}.mkv'.format(output)], shell=False)

    def stream(self, connection, client):
        self.camera.annotate_text = self._timestamp('%Y-%m-%d %H:%M:%S')
        self.camera.start_recording(connection, format='h264')

        try:
            while True:
                self.camera.annotate_text = self._timestamp('%Y-%m-%d %H:%M:%S')
                self.camera.wait_recording(0.3)
        except KeyboardInterrupt:
            pass
        finally:
            print('Shutting down camera.')
            self.camera.stop_recording()
            print('Shutting down client.')
            client.close()
            print('Shutting down server connection.')
            connection.close()

    def _timestamp(self, timecodes='%Y-%m-%d_%H_%M_%S'):
        return dt.datetime.now().strftime(timecodes)






