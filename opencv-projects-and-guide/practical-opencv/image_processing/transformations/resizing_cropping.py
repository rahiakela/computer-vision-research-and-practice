import cv2
import numpy as np
import config

img = cv2.imread(config.GLOBAL_IMG_PATH + "lambo.png")
print(img.shape)

# resize image
img_resized = cv2.resize(img, (1000, 500))
print(img_resized.shape)

# crop image
img_cropped = img[0:200, 200:500]

cv2.imshow("Image", img)
# cv2.imshow("Resized Image", img_resized)
cv2.imshow("Cropped Image", img_cropped)
cv2.waitKey(0)
