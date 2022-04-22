from machine import Pin
import time

pin = Pin('PC13', Pin.IN)
while True:
    if pin.value():
        print("Human detected")
    else:
        print("No human detected")
    time.sleep(0.5)
