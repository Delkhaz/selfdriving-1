'''
MTSU Makers: Self Driving Car

main.py will manage the image capture and instruction set

'''

import cv2
import numpy as np

# init camera
camera = cv2.VideoCapture(0)

def get_image():
	'''
	Returns the np.ndarray of the image, 480x640x3
	'''
	_, im = camera.read()
	return im


while True:
	im = get_image()

	cv2.imshow('ImageWindow', im)
	cv2.waitKey(0)
	break
im[np.where(im[::0]<=175)]=0
cv2.imshow("newim", im)
