#import serial 
from serial import *
import time
from struct import *

seriaL = Serial('/dev/ttyUSB1', 9600)   # open serial port that Arduino is using

time.sleep(2)				# ardiuno reset when you open serial port

#print(seriaL.portstr)			# checks if port was really used
#print(seriaL)		

# Sends RPM (number) and wheel instructions to arduino
def SetWheels(opCode, number):
    message = pack('Bh',opCode,number)
    seriaL.write(message)

def StopWheels():
    message = pack('B',ord('S'))
    seriaL.write(message)
userOp = ord(input("opCode: ")[0])
numbero = int(input("number: "))

SetWheels(userOp,numbero)

time.sleep(3)

StopWheels()

seriaL.close()
