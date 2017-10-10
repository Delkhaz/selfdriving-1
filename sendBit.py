#import serial 
from serial import *
import time
from struct import *

			 
#seriaL = serial.Serial('/dev/ttyUSB0', 9600)   # open serial port that Arduino is using

seriaL = Serial('/dev/ttyUSB0', 9600)   # open serial port that Arduino is using

time.sleep(4)				# ardiuno reset when you open serial port

print(seriaL.portstr)			# checks if port was really used
print(seriaL)		

#print("Sending Hi to serial data") 
#seriaL.write("Hi")			# writes a string
#seriaL.close()				# close port 

					# close connection 
#if( seriaL.isOpen()):
 #   print(" serial is open still ") 
  #  seriaL.close()

# Sends RPM (number) and wheel instructions to arduino
def SetWheels(opCode, number):
    message = pack('Bh',opCode,number)
    seriaL.write(message)

def StopWheels():
    message = pack('B','S')
    seriaL.write(message)
#user.op = input("opCode: "); 
userOp = str.decode(input("opCode: "),'utf-8')
numbero = int(input("number: "))

SetWheels(userOp,numbero)

time.sleep(5)

StopWheels()

seriaL.close()
