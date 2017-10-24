#!/usr/bin/env python3
'''
MTSU Makers: Self Driving Car

main.py will manage the image capture and instruction set

'''



import cv2
import matplotlib.pyplot as plt
import numpy as np
from serial import *
from struct import *
import time

seriaL = Serial('/dev/ttyUSB0', 9600)
time.sleep(2)

# Sends RPM (number) and wheel instructions to arduino
def SetWheels(opCode, number):
    message = pack('Bh',ord(opCode),number)
    seriaL.write(message)

def StopWheels():
    message = pack('B',ord('S'))
    seriaL.write(message)

ESC_KEY = 27

# init camera
camera = cv2.VideoCapture(0)

state = "forward"
MAX_SPEED = 1000
SPEED_STEP = 50
speed = MAX_SPEED

while True:
	if state == "forward":
		# 
		_, image= camera.read()
		# Convert to hsv color space
		hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
		# Create ranges for HSV space (red)
		mask = cv2.inRange(hsv, np.array((0, 120,40)), np.array((20, 255, 255)))
		# Apply the mask to the image
		output = cv2.bitwise_and(image, image, mask = mask)
		gray = cv2.cvtColor(output, cv2.COLOR_HSV2BGR)
		gray = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY)
		_, thresh = cv2.threshold(gray, 127,255,0, cv2.THRESH_TOZERO)
		thresh = cv2.medianBlur(thresh, 5)
		_,contours,h = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
		# show the images
		for cnt in contours:
			num_sides = len(cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),False))
			if num_sides >= 7 and num_sides <= 10:
				area=cv2.contourArea(cnt)
				if area >= 1250:
					cv2.drawContours(output, [cnt], 0, (0,255,0), -1)
					center = tuple(np.mean(cnt, axis=0)[0].astype(int))
					cv2.circle(output, center, 5, (255,0,0), SPEED_STEP)
					print("Found a stop sign at {} with area {}".format(center, area)) 
					state = "stopping"
		# cv2.drawContours(output, contours, -1, (0,255,0), SPEED_STEP)
		# cv2.imshow("images", cv2.resize(output, (320,240))) 
		# Break the esc loop
		if cv2.waitKey(1) == ESC_KEY:
			break
	elif state == "stopping":
		if speed > 0:
			speed -= SPEED_STEP
			time.sleep(0.1)
		else:
			state = "stopped"
	elif state == "stopped":
		time.sleep(5)
		state = "forward"
	print("moving forward at {} speed".format(speed))
	SetWheels('B', speed)

seriaL.close()
