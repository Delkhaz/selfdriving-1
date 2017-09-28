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
	# Create ranges for HSV space (red)
	mask1 = cv2.inRange(hsv, np.array((0, 70,50)), np.array((10, 255, 255)))
	mask2 = cv2.inRange(hsv, np.array((165, 70,50)), np.array((180, 255, 255)))	
	mask = cv2.bitwise_or(mask1, mask2);
	# Apply the mask to the image
	output = cv2.bitwise_and(image, image, mask = mask)
	gray = cv2.cvtColor(output, cv2.COLOR_HSV2BGR)
	gray = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY)
	_, thresh = cv2.threshold(gray, 127,255,0)
	thresh = cv2.inpaint(thresh,cv2.bitwise_not(cv2.bitwise_xor(thresh, thresh)),3,cv2.INPAINT_TELEA)
	_,contours,h = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	# show the images
	for cnt in contours:
		num_sides = len(cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),False))
		if num_sides >= 7 and num_sides <= 10:
			cv2.drawContours(output, [cnt], 0, 255, -1)
	#cv2.drawContours(output, contours, -1, (0,255,0), 3)
	cv2.imshow("images", thresh)
	#cv2.imshow("images", np.hstack([image, output]))
	# Break the esc loop
	if cv2.waitKey() == ESC_KEY:
		break
