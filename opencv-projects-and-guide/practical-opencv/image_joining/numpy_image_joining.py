import cv2
import numpy as np
import config

img = cv2.imread(config.GLOBAL_IMG_PATH + "lena.png")
cv2.imshow("Original", img)

# stack horizontally
img_horizontal = np.hstack([img, img])
cv2.imshow("Horizontal", img_horizontal)

# stack vertically
img_vertical = np.vstack([img, img])
cv2.imshow("Vertical", img_vertical)

cv2.waitKey(0)
