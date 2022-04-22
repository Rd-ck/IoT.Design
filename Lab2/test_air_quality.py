from machine import Pin, I2C
import time
from CCS811 import  CCS811

# Pull nWake to ground to wake up CCS811
wake = Pin('PB12', Pin.OUT)
wake.off()

i2c = I2C(1)
s = CCS811(i2c)
time.sleep(1)

while True:
    if s.data_ready():
        print('eCO2: %d ppm, TVOC: %d ppb' % (s.eCO2, s.tVOC))
        time.sleep(1)
