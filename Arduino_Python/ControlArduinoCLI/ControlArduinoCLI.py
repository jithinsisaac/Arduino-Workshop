import serial
import time

ArduinoSerial = serial.Serial('COM7',9600)
time.sleep(2)


while 1:

    print ("Enter 1 to turn ON LED and 0 to turn OFF LED")
    var = input()
    print ("You entered: ", var)

    if (var == '1'):
        ArduinoSerial.write(b'1')

    if (var == '0'):
        ArduinoSerial.write(b'0')
