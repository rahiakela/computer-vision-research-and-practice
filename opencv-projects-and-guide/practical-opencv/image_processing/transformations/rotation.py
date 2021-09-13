import numpy as np
import cv2
import config
from imutils import rotate

img = cv2.imread(config.GLOBAL_IMG_PATH + "trex.png")
cv2.imshow("Original", img)
cv2.waitKey(0)

# grabs the width and height of the image
(h, w) = img.shape[:2]
# then divides each by 2 to determine the center
center = (w // 2, h // 2)

# rotate the image 45 degrees and scale of the image the same dimensions of the image
M = cv2.getRotationMatrix2D(center, 45, 1.0)
# apply the rotation to the image
rotated = cv2.warpAffine(img, M, (w, h))
cv2.imshow("Rotated by 45 Degrees", rotated)
cv2.waitKey(0)

# rotate the image 45 degrees and scale of the image is doubled in size
M = cv2.getRotationMatrix2D(center, 45, 2.0)
rotated = cv2.warpAffine(img, M, (w, h))
cv2.imshow("Rotated by 45 Degrees", rotated)
cv2.waitKey(0)

M = cv2.getRotationMatrix2D(center, -90, 1.0)
rotated = cv2.warpAffine(img, M, (w, h))
cv2.imshow("Rotated by -90 Degrees", rotated)
cv2.waitKey(0)

rotated = rotate(img, 180)
cv2.imshow("Rotated by 180 Degrees", rotated)
cv2.waitKey(0)

# Rotated by 360 Degrees, means back to original
rotated = rotate(img, 360)
cv2.imshow("Rotated by 360 Degrees", rotated)
cv2.waitKey(0)
