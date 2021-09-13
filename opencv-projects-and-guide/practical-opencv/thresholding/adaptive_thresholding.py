import numpy as np
import cv2
import config

"""
we can use adaptive thresholding, which considers small neighbors of pixels
and then finds an optimal threshold value T for each neighbor.
"""

img = cv2.imread(config.GLOBAL_IMG_PATH + "coins.png")
cv2.imshow("Original", img)

# first of all, convert image to grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Applying Gaussian blurring helps remove some of the high frequency edges in the image
# that we are not concerned with.
blurred = cv2.GaussianBlur(img_gray, (5, 5), 0)
cv2.imshow("Blurred", blurred)

# apply adaptive thresholding to blurred image by computing the mean of the neighborhood(neighborhood size 11) of pixels
mean_thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 4)
cv2.imshow("Mean Thresh", mean_thresh)

# apply Gaussian adaptive thresholding to blurred image by computing the weighted mean of the neighborhood(neighborhood size 15) of pixels
gaussian_thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 15, 3)
cv2.imshow("Gaussian Thresh", gaussian_thresh)

cv2.waitKey(0)
