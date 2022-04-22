from machine import Pin, SPI
import time
from sx127x import SX127x

device_pins = {'ss':'PB6', 'dio_0': 'PC6', 'reset':'PC7' }
device_spi = SPI(1)

lora = SX127x(device_spi, pins=device_pins)

while True:
    lora.send('hello lora'.encode())
    time.sleep(3)
