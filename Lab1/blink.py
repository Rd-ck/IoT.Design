from machine import Pin
import time

red_led = Pin('PC8', Pin.OUT)

while True:
    red_led.off()
    time.sleep(1)
    red_led.on()
    time.sleep(1)
