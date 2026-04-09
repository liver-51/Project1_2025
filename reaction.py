from gpiozero import LED, Button
from time import sleep
from random import uniform

led = LED(4)
left_btn = Button(14)
right_btn = Button(15)

led.on()
sleep(uniform(5, 10))
led.off()

def pressed(btn):
    print(f"Button {btn.pin.number} pressed!")

left_btn.when_pressed = pressed
right_btn.when_pressed = pressed

while True:
    sleep(0.1)
