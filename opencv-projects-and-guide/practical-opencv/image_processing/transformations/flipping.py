import cv2
import numpy as np
import config

img = cv2.imread(config.GLOBAL_IMG_PATH + "trex.png")
cv2.imshow("Original", img)

# 1 indicates to flip the image horizontally, around the y-axis
flipped =cv2.flip(img, 1)
cv2.imshow("Flipped Horizontally", flipped)

# 0 indicates to flip the image vertically, around the x-axis
flipped = cv2.flip(img, 0)
cv2.imshow("Flipped Vertically", flipped)

# -1 indicates to flip the image horizontally and vertically
flipped = cv2.flip(img, -1)
cv2.imshow("Flipped Horizontally & Vertically", flipped)

cv2.waitKey(0)
