from etc import mqtt_publish as m_p
from etc import config as conf
import json
import time
import socket
from etc import value


with open('format/temperature_json_format.json') as json_file:
    msg = json_file.read()
    device_code = '001'
    lan = socket.gethostbyname(socket.gethostname())

while True : 
    time_num = int(time.time())


    external_value = value.call_external_temp()
    tmp = int(external_value[0:2])
    inner_value = str(tmp - 3)
    
    m_p.mqtt_publish(msg % (device_code, time_num, lan, conf.broker_ip, external_value, inner_value))
    time.sleep(conf.call_delay('temp'))












