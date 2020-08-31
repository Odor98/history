import paho.mqtt.client as mqtt
import config as conf

def on_connect(client, userdata, flags, rc):
    print("connection with result code " + str(rc))


    client.subscribe(conf.topic)


def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(conf.broker_ip)
client.loop_forever()
