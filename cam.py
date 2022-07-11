from time import sleep
from picamera import PiCamera

camera = PiCamera(resolution=(1024, 768))
# camera.resolution = (1024, 768)
camera.rotation = 180
camera.annotate_text = 'Foo'
camera.start_preview()
# Camera warm-up time
sleep(2)
camera.capture('foo.jpg')

sleep(2)

camera.start_recording('foovid.h264')

camera.wait_recording(5)

camera.stop_recording()

