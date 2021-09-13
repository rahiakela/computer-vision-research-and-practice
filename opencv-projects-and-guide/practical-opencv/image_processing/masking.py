import cv2
import numpy as np
import config

"""
Using a mask allows us to focus only on the portions of
the image that interests us.
"""

img = cv2.imread(config.GLOBAL_IMG_PATH + "beach.png")
cv2.imshow("Original", img)

# compute the center of the image by dividing the width and height by 2
mask = np.zeros(img.shape[:2], dtype="uint8")
(cX, cY) = (img.shape[1] // 2, img.shape[0] // 2)
cv2.rectangle(mask, (cX - 75, cY - 75), (cX + 75, cY + 75), 255, -1)
cv2.imshow("Mask", mask)

masked = cv2.bitwise_and(img, img, mask=mask)
cv2.imshow("Masked", masked)

# create circle mask
mask = np.zeros(img.shape[:2], dtype="uint8")
cv2.circle(mask, (cX, cY), 100, 255, -1)
masked = cv2.bitwise_and(img, img, mask=mask)
cv2.imshow("Mask Applied to Image", masked)

cv2.waitKey(0)
