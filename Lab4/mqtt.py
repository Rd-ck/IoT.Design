from paho.mqtt import client as mqtt_client
import data
import random

broker = 'aliyun.zstu.tech'
port = 1883
topic = "Rdcc" # 修改为与底板上程序相同的topic
client_id = f'cid-{random.randint(0, 1000)}'
data.drop()
data.create()


def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def subscribe(client):
    def on_message(client, userdata, msg):
        payload = msg.payload.decode()
        print(f"Received %s from %s topic" % (payload, msg.topic))
        tem = float(payload[14:19])
        data.insert(tem)
        
    client.subscribe(topic)
    client.on_message = on_message


client = connect_mqtt()
subscribe(client)
client.loop_forever()
