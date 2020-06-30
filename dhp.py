#!/usr/bin/python

import time
import Adafruit_DHT
import pymysql

sensor = Adafruit_DHT.DHT11

pin = 2

while(True):
	humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
	
	time.sleep(60)
	if humidity is not None and temperature is not None:
		conn = pymysql.connect(host='192.168.0.14', user='suk', password='1234', db='AA')
		c = conn.cursor()

		sql = "insert into inside_temp values('{0}', '{1}', '{2}%')".format(int(time.time()), temperature, humidity)
		print(sql)

		c.execute(sql)
		conn.commit()
		conn.close()
		
