"""
The Canny edge detector is a multi-step process. It involves
blurring the image to remove noise, computing Sobel gradient
images in the x and y direction, suppressing edges, and
finally a hysteresis thresholding stage that determines if a
pixel is “edge-like” or not.
"""
import cv2
import config
import numpy as np


img = cv2.imread(config.GLOBAL_IMG_PATH + "coins.png")
# convert to gray
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# blur it using the Gaussian blurring method
img_blurred = cv2.GaussianBlur(img_gray, (5, 5), 0)
cv2.imshow("Image Blurred", img_blurred)

# applying the Canny edge detector using threshold 1 and threshold 2
img_canny = cv2.Canny(img_blurred, 30, 150)
cv2.imshow("Image Canny", img_canny)

cv2.waitKey(0)
