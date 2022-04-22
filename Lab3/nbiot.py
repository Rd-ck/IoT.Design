import time
from machine import UART
import weather

def at(s, timeout=0.5):
    uart.write((s+'\r\n').encode())
    time.sleep(timeout)
    s = uart.read()
    if s != None:
        s = s.decode()
        print(s)
    return s

uart = UART(1, 9600)
at("AT")
at("AT+SM=LOCK")
at("AT+CMEE=1")

def wait_connection():
    while True:
        try:
            s = uart.read()
            if s != None:
                print(s.decode())
            print("AT+CGATT?")
            s = at("AT+CGATT?", 1)
            print("s=%s" % s)
            if "+CGATT: 1" in s:
                print("Success!")
                break
            print("AT+CSQ")
            at("AT+CSQ")
        except Exception:
            print("err, try again")
        finally:
            time.sleep(1)

def mqtt_conn():
    global client_name
    at('AT+QMTOPEN=0,"aliyun.zstu.tech",1883')
    time.sleep(3)
    at('AT+QMTCONN=0,"%s"' % client_name, 1)
    time.sleep(1)

def mqtt_pub(topic, msg):
    at('AT+QMTPUB=0,0,0,0,"%s","%s"' % (topic, msg))

client_name = "student_%d" % time.time()
wait_connection()
mqtt_conn()

while True:
    at("AT") # wakeup
    mqtt_pub("Rdcc", "Temperture is %s, client: %s" % (weather.get_temperature(),client_name))
    time.sleep(5)
