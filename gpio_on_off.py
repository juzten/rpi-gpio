from gpiozero import LED, Button
import RPi.GPIO as GPIO
from time import sleep

led = LED(17)
button = Button(2)

while True: 
    button.when_pressed = led.on
    button.when_released = led.off
