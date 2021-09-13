import numpy as np
import cv2
import mahotas
import config

"""
Another way we can automatically compute the threshold value of T is to use Otsu’s method.
Otsu’s method assumes there are two peaks in the grayscale
histogram of the image. It then tries to find an optimal
value to separate these two peaks – thus our value of T.
"""

img = cv2.imread(config.GLOBAL_IMG_PATH + "coins.png")
cv2.imshow("Original", img)

# first of all, convert image to grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Applying Gaussian blurring helps remove some of the high frequency edges in the image that we are not concerned with.
blurred = cv2.GaussianBlur(img_gray, (5, 5), 0)
# cv2.imshow("Blurred", blurred)

# compute optimal value of T
T = mahotas.thresholding.otsu(blurred)
print("Otsu's threshold: {}".format(T))

# Applying the thresholding
thresh = img.copy()
thresh[thresh > T] = 255
thresh[thresh < 255] = 0
thresh = cv2.bitwise_not(thresh)
cv2.imshow("Otsu", thresh)

T = mahotas.thresholding.rc(blurred)
print("Riddler-Calvard:{}".format(T))
thresh = img.copy()
thresh[thresh > T] = 255
thresh[thresh < 255] = 0
thresh = cv2.bitwise_not(thresh)
cv2.imshow("Riddler-Calvard", thresh)

cv2.waitKey(0)
