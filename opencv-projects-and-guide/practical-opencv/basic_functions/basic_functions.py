import cv2
import config
import numpy as np

img = cv2.imread(config.GLOBAL_IMG_PATH + "lena.png")

# define kernel
kernel  = np.ones((5, 5), np.uint8)

# change image color
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blurred = cv2.GaussianBlur(img_gray, (7, 7), 0)  # with kernel (7, 7)
img_canny = cv2.Canny(img, 150, 200)                 # threshold value 100 and 100
img_dilation = cv2.dilate(img_canny, kernel, iterations=2)
img_eroded = cv2.erode(img_dilation, kernel, iterations=1)

# cv2.imshow("Gray Image", img_gray)
# cv2.imshow("Blurred Image", img_blurred)
cv2.imshow("Canny Image", img_canny)
cv2.imshow("Dilation Image", img_dilation)
cv2.imshow("Eroded Image", img_eroded)

cv2.waitKey(0)
