import cv2
import numpy as np

# define image matrix
img = np.zeros((512, 512, 3), np.uint8)
print(img.shape)

# change color of image
img[:] = (255, 0, 0)

# create line
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 0, 255), 3)
cv2.line(img, (0, img.shape[1]), (img.shape[1], 0), (0, 255, 0), 3)

# create rectangle
cv2.rectangle(img, (0, 0), (250, 350), (0, 0, 255), 2)

# create circle
cv2.circle(img, (400, 50), 30, (255, 255, 0), 5)
cv2.circle(img, (400, 150), 30, (255, 255, 0), 5)

# append some text
cv2.putText(img, " OPENCV ", (300, 200), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 3)

cv2.imshow("Image", img)
cv2.waitKey(0)

