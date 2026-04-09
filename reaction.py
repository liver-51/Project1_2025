from gpiozero import LED
from time import sleep
from random import uniform

led = LED(4)
led.on()
sleep(uniform(5, 10))
led.off()
