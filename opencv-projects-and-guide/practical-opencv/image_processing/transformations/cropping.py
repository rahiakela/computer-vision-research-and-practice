import cv2
import numpy as np
import config

img = cv2.imread(config.GLOBAL_IMG_PATH + "trex.png")
cv2.imshow("Original", img)

# NumPy array slices to extract a rectangular region of the image
img_cropped = img[30:120, 240:335]
cv2.imshow("T-Rex Face", img_cropped)

cv2.waitKey(0)
