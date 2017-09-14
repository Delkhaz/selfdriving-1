'''
MTSU Makers: Self Driving Car

main.py will manage the image capture and instruction set

'''

import cv2
import numpy as np

# just a rough draft for now

camera = cv2.VideoCapture(0)

def get_image():
	_, im = camera.read()
	return im


