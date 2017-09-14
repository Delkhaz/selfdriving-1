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

	# trying to display image via PIL instead.
	# currently not working
	im_PIL = Image.new("RGB", (480,640), "white")
	im_PIL.putdata(im)
	im_PIL.show()
	#cv2.imshow('ImageWindow', im)
	cv2.waitKey(0)
