from machine import I2C, Pin
import time
import tcs34725

i2c = I2C(1)
sensor = tcs34725.TCS34725(i2c)
sensor.gain(16)
sensor.integration_time(402)

sensor.active(True)
time.sleep_ms(500)
while True:
    try:
        data = sensor.read(True)
        print(tcs34725.html_hex(data))
    except Exception as e:
        print("put it further away")
    finally:
        time.sleep_ms(200)
