from machine import Pin, I2C
from BMI160 import BMI160_I2C
from time import sleep_ms

i2c = I2C(1)
bmi160 = BMI160_I2C(i2c, addr=0x68)
while True:
    print("{0:>8}{1:>8}{2:>8}{3:>8}{4:>8}{5:>8}".format(*bmi160.getMotion6()))
    sleep_ms(1000//25)
