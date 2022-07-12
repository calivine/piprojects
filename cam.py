from time import sleep
from picamera import PiCamera
from led import Led

camera = PiCamera(resolution=(1024, 768))
led = Led(4)
# camera.resolution = (1024, 768)
camera.rotation = 180
camera.annotate_text = 'Foo'
camera.start_preview()
# Camera warm-up time
sleep(2)
camera.capture('foo.jpg')

sleep(2)

camera.start_recording('foovid.h264')
led.turn_on()

camera.wait_recording(5)

camera.stop_recording()
led.turn_off()

