from machine import UART
import time

def wait(timeout):
    for i in range(timeout / 10):
        time.sleep_ms(10)
        if uart.any():
            print(uart.read(1024).decode(), end='')
    print()

def at(cmd, timeout=100):
    uart.write('AT+' + cmd + '\r')
    wait(timeout)

def mqtt_pub(msg, timeout=100):
    at('MQTTSEND=%d' % len(msg), timeout)
    uart.write(msg)

uart = UART(3, 115200)

# connect
at('WJAP=这里要改成WiFi无线路由器的SSID,改成WiFi密码',5000)

# query IP
at('WJAPIP?')

client_name = "client_%d" % time.time()
# MQTT
at('MQTTCID=%s' % client_name, 1000)
at('MQTTEVENT=ON',1000)
at('MQTTSOCK=aliyun.zstu.tech,1883', 1000)
at('MQTTSTART', 1000)

at('MQTTPUB=mytopic,0')

while True:
    mqtt_pub('Hello from WiFi')
    time.sleep(1)

at('MQTTCLOSE')
