'''
MTSU Makers: Self Driving Car

main.py will manage the image capture and instruction set

'''

import cv2
import numpy as np
from PIL import Image

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
	#im.show()	
	# create NumPy arrays from the boundaries
	lower = np.array([0,0,80], dtype = "uint8")
	upper = np.array([50,50,255], dtype = "uint8")
	# find the colors within the specified boundaries and apply
	# the mask
	mask = cv2.inRange(image, lower, upper)
	output = cv2.bitwise_and(image, image, mask = mask)
	# show the images
	cv2.imshow("images", np.hstack([image, output]))
	cv2.waitKey(0)
