import paho.mqtt.client as mqtt
import time
import json
import config as conf


def mqtt_publish(msg):
    mqtt_p = mqtt.Client()
    mqtt_p.connect(conf.broker_ip, 1883)

    mqtt_p.publish(conf.topic, msg)
    print(msg)


if __name__ == '__main__':
    mqtt_publish('temp')
