import RPi.GPIO as GPIO
import dht11

from time import *

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

while True:

    instance = dht11.DHT11(pin=4)
    result = instance.read()

    # Uncomment for Fahrenheit:
    result.temperature = (result.temperature * 1.8) + 32
    if result.is_valid():
        print(strftime("%A, %d %B %Y, %X", localtime()))
        print("Temp: %d%s F" % (result.temperature, chr(1)))
        print("Temp. {}{}F".format(result.temperature, chr(176)))
        print("Humidity: %d %%" % result.humidity)
    sleep(30)
