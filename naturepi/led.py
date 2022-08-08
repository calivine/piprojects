from gpiozero import LED


class Led:

    def __init__(self, pin):
        self.light = LED(pin)

    def turn_on(self):
        self.light.on()

    def turn_off(self):
        self.light.off()

