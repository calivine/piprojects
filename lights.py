from time import sleep

from led import Led

red = Led(4)

green = Led(17)

while True:
    red.turn_on()
    sleep(5)
    red.turn_off()
    sleep(5)
    green.turn_on()
    sleep(5)
    green.turn_off()


