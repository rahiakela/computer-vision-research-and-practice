"""
Translation is the shifting of an image along the x and y
axis. Using translation, we can shift an image up, down,
left, or right, along with any combination of the above!
"""

import cv2
import numpy as np
import config
from imutils import translate

img = cv2.imread(config.GLOBAL_IMG_PATH + "trex.png")
cv2.imshow("Original", img)

# translation matrix that tells us how many pixels to the left or right, and up or down,
# the image will be shifted.
M = np.float32([
    [1, 0, 25],  # [1, 0, Tx] for shifting left or right
    [0, 1, 50]   # [1, 0, Ty] for shifting up or down
])               # so shifting the image 25 pixels to the right and 50 pixels down.
shifted = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
cv2.imshow("Shifted Down and Right", shifted)

"""
shifting the image 50 pixels to the left and 90 pixels up. 
The image is shifted left and up rather than right and
down, because we are providing a negative values for both tx and ty.
"""
M = np.float32([
    [1, 0, -50],
    [0, 1, -90]
])
shifted = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
cv2.imshow("Shifted Up and Left", shifted)

# shift the image 100 pixels down
shifted = translate(img, 0, 100)
cv2.imshow("Shifted down", shifted)

cv2.waitKey(0)
