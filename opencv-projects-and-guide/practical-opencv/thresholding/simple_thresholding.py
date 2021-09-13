import numpy as np
import cv2
import config

"""
Thresholding is often used as a method to segment the foreground of an image from the background.

Thresholding is the binarization of an image.
Normally, we use thresholding to focus on objects or areas of particular interest in an image.
Applying simple thresholding methods requires human intervention.
We must specify a threshold value T.
"""

img = cv2.imread(config.GLOBAL_IMG_PATH + "coins.png")
cv2.imshow("original", img)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Applying Gaussian blurring helps remove some of the high frequency edges in the image
# that we are not concerned with.
blurred = cv2.GaussianBlur(img_gray, (5, 5), 0)
cv2.imshow("Blurred", blurred)

# compute the threshold by supplying T threshold value 155
(T, thresh) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY)
print(T)
cv2.imshow("Threshold Binary", thresh)

# apply inverse thresholding
(T, thresh_inv) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY_INV)
print(T)
cv2.imshow("Threshold Binary Inverse", thresh_inv)

cv2.waitKey(0)
