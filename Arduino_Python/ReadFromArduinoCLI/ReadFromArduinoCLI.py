import serial
import time

ArduinoSerial = serial.Serial('COM7',9600)
time.sleep(2)


while 1:

	if (ArduinoSerial.inWaiting()>0):
		myData = ArduinoSerial.readline()
	print (myData)
	time.sleep(1)
