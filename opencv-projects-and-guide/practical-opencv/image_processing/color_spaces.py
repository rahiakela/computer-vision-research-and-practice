import numpy as np
import cv2
import config

img = cv2.imread(config.GLOBAL_IMG_PATH + "beach.png")
cv2.imshow("Original", img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", hsv)

lab = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Lab", gray)

cv2.waitKey(0)
