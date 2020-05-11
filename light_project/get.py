import time
import spidev

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz=1000000

def ReadVol(vol):
	adc = spi.xfer2([1, (8+vol)<<4,0])
	data=((adc[1]&3)<<8)+adc[2]
	return data





while True:
	a_1 = ReadVol(0)
	a_2 = ReadVol(1)
	a_3 = ReadVol(2)
	print('readvol : ', a_1, 'voltage:', 3.3*a_1/1024)
	print('readvol : ', a_2, 'voltage:', 3.3*a_2/1024)
	print('readvol : ', a_3, 'voltage:', 3.3*a_3/1024)
	time.sleep(0.5)


