"""
Formally, edge detection embodies mathematical
methods to find points in an image where the
brightness of pixel intensities changes distinctly.
"""
import cv2
import config
import numpy as np


img = cv2.imread(config.GLOBAL_IMG_PATH + "coins.png")
# convert to gray
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", img_gray)

# compute the gradient magnitude image by using Laplacian method
img_laplacian = cv2.Laplacian(img_gray, cv2.CV_64F)
img_laplacian = np.uint8(np.absolute(img_laplacian))
cv2.imshow("Laplacian", img_laplacian)

# compute the gradient representation
sobelX = cv2.Sobel(img_gray, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(img_gray, cv2.CV_64F, 0, 1)

# find all edges by taking the absolute value of the floating point image and
# then converting it to an 8-bit unsigned integer.
sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

# In order to combine the gradient images in both the x and y direction, we can apply a bitwise OR.
sobel_combined = cv2.bitwise_or(sobelX, sobelY)
cv2.imshow("Sobel X", sobelX)
cv2.imshow("Sobel Y", sobelY)
cv2.imshow("Sobel Combined", sobel_combined)

cv2.waitKey(0)
