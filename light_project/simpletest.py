import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

while True:
	now = time.localtime()	
	#s = "%04d-%02d-%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
	s = int(time.time())
	values = [0]*3
	for i in range(3):
		values[i] = mcp.read_adc(i)

	print('[ID : 0, ' + 'time : ' + str(s) + ', value : {0:>4}]'.format(*values))
	print('[ID : 1, ' + 'time : ' + str(s) + ', value : {1:>4}]'.format(*values))
	print('[ID : 2, ' + 'time : ' + str(s) + ', value : {2:>4}]'.format(*values))
	time.sleep(0.5)
