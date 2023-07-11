from machine import Pin
import time
led = Pin(12, Pin.OUT)
button = Pin(13, Pin.IN)
while True:
    if button.value() == 1:
        led.value(0)
    else:
        led.value(1)