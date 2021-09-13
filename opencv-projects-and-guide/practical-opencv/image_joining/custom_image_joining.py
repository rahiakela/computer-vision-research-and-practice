import cv2
import numpy as np
import config
from global_utils import stackImages


img = cv2.imread(config.GLOBAL_IMG_PATH + "lena.png")
cv2.imshow("Original", img)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img_stack = stackImages(0.5, ([img, img_gray, img], [img, img, img_gray]))

cv2.imshow("ImageStack", img_stack)
cv2.waitKey(0)
