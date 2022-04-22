import dht
import time
from machine import Pin

d = dht.DHT11(Pin('PC13'))
while True:
    d.measure()
    print("TEMP: %d, Humidity: %d" % (d.temperature(), d.humidity()))
    time.sleep(1)
