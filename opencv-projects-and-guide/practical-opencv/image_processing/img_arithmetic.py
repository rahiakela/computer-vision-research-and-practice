"""
However, be sure to keep in mind that there is a difference
between OpenCV and NumPy addition. NumPy will
perform modulo arithmetic and “wrap around”. OpenCV,
on the other hand, will perform clipping and ensure pixel
values never fall outside the range [0, 255].
"""
import numpy as np
import cv2
import config

img = cv2.imread(config.GLOBAL_IMG_PATH + "trex.png")
cv2.imshow("Original", img)

# difference between OpenCV and NumPy addition
print("max of 255: {}".format(cv2.add(np.uint8([200]), np.uint8([100]))))
print("min of 0: {}".format(cv2.subtract(np.uint8([50]), np.uint8([100]))))
print("wrap around: {}".format(np.uint8([200]) + np.uint8([100])))
print("wrap around: {}".format(np.uint8([50]) - np.uint8([100])))

# perform the arithmetic on actual images
M = np.ones(img.shape, dtype="uint8") * 100  # fill matrix with values of 100’s rather than 1’s
img_added = cv2.add(img, M)
cv2.imshow("Image Added", img_added)

M = np.ones(img.shape, dtype="uint8") * 50  # fill matrix with values of 50’s rather than 1’s
img_subtracted = cv2.subtract(img, M)
cv2.imshow("Image Subtracted", img_subtracted)

cv2.waitKey(0)
