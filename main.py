'''
MTSU Makers: Self Driving Car

main.py will manage the image capture and instruction set

'''

import cv2
import numpy as np

ESC_KEY = 27

# init camera
camera = cv2.VideoCapture(0)

while True:
	# Read camera image
	_, image= camera.read()
	# Convert to hsv color space
	hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
	#im.show()	
	# create NumPy arrays from the boundaries
	# COLORS ARE BGR
	lower = np.array([0,0,80], dtype = "uint8")
	upper = np.array([80,80,255], dtype = "uint8")
	# Create ranges for HSV space (red)
	mask1 = cv2.inRange(hsv, np.array((0, 70, 50)), np.array((10, 255, 255)))
	mask2 = cv2.inRange(hsv, np.array((170, 70, 50)), np.array((180, 255, 255)))
	# the mask
	mask = cv2.bitwise_or(mask1, mask2); 
	output = cv2.bitwise_and(image, image, mask = mask)
	# show the images
	cv2.imshow("images", np.hstack([image, output]))
	if cv2.waitKey() == ESC_KEY:
		break
