from machine import Pin, I2C
from time import sleep
import BME280

i2c = I2C(1)
bme = BME280.BME280(i2c=i2c)

while True:
    print('Temperature: ', bme.temperature,
          'Humidity: ', bme.humidity,
          'Pressure: ', bme.pressure)
    sleep(1)
