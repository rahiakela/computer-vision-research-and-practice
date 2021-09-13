import cv2
import numpy as np
import config
from imutils import resize

"""
When resizing an image, we need to keep in mind
the aspect ratio of the image. The aspect ratio is the proportional
relationship of the width and the height of the image.
If we aren’t mindful of the aspect ratio, our resizing will
return results that don’t look correct.
"""

img = cv2.imread(config.GLOBAL_IMG_PATH + "trex.png")
cv2.imshow("Original", img)

"""
In order to compute the ratio of the new height to
the old height, we simply define our ratio r to be the new
width (150 pixels) divided by the old width.
"""
r = 150.0 / img.shape[1]   # resize the image by specifying the width
# compute the new dimensions of the image
dim = (150, int(img.shape[0] * r))
# interpolation method handle the actual image is resizing
resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("Resized (Width)", resized)

# resize the image by specifying the height
r = 50.0 / img.shape[0]
dim = (int(img.shape[0] * r), 50)
resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("Resized (Height)", resized)

# resize the image using custom func
resized = resize(img, width=100)
cv2.imshow("Resized via Function", resized)

# resize the image using custom func
resized = resize(img, height=50)
cv2.imshow("Resized via Function2", resized)

cv2.waitKey(0)