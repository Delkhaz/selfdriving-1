import numpy as np
from PIL import Image
import os
from skimage.feature import blob_doh


IMG_PATH = os.path.join("imgs", "womaD.png")
# all channels the same in this test image
X = np.array(Image.open(IMG_PATH))[:,:,0]
#X[np.where(X>0)] = 1
X = np.divide(X, X.max()) 

blobs_doh = blob_doh(X, max_sigma=30, threshold=0.1)
