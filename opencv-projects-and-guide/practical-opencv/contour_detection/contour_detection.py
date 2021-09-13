import numpy as np
import cv2
import config
from global_utils import stackImages, get_contours

img = cv2.imread(config.GLOBAL_IMG_PATH + "shapes.png")
img_contour = img.copy()
# cv2.imshow("Original", img)


img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blurred = cv2.GaussianBlur(img_gray, (7, 7), 1)
img_canny = cv2.Canny(img_blurred, 50, 50)

get_contours(img_canny, img_contour)

img_blank = np.zeros_like(img)

img_stack = stackImages(0.6, (
    [img, img_gray, img_blurred],
    [img_canny, img_contour, img_blank]
))
# cv2.imshow("Gray", img_gray)
# cv2.imshow("Blurred", img_blurred)
cv2.imshow("Stack", img_stack)

cv2.waitKey(0)
