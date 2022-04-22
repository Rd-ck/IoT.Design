from pyb import Pin, ADC
import time

adc = ADC(Pin('PC2'))
while True:
    print(adc.read())
    time.sleep(1)
