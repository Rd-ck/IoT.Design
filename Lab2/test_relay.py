from pyb import Pin
import time

relay1 = Pin('PB1', Pin.OUT)
relay2 = Pin('PB12', Pin.OUT)
while True:
    relay1.on()
    time.sleep(1)
    relay1.off()
    time.sleep(1)

    relay2.on()
    time.sleep(1)
    relay2.off()
    time.sleep(1)
