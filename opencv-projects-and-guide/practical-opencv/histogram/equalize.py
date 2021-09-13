import numpy as np
import cv2
import config

"""
Histogram equalization is normally useful when enhancing the contrast of
medical or satellite images and an X-ray.

"""

img = cv2.imread(config.GLOBAL_IMG_PATH + "beach.png")
cv2.imshow("Original", img)

image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
equalize = cv2.equalizeHist(image)
cv2.imshow("Histogram Equalization", np.hstack([image, equalize]))

cv2.waitKey(0)
