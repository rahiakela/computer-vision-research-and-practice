import numpy as np
import cv2
import config


img = cv2.imread(config.GLOBAL_IMG_PATH + "wave.png")
cv2.imshow("Original", img)

# Splitting the image based on channels
(B, G, R) = cv2.split(img)
cv2.imshow("Red", R)
cv2.imshow("Green", G)
cv2.imshow("Blue", B)

# merge image using channels
merged = cv2.merge([B, G, R])
cv2.imshow("Merged", merged)

# take apart the image to show the actual “color” of the channel
# Then, we need to re-construct the image, but this time setting all pixels but the current channel as zero.
zeros = np.zeros(img.shape[:2], dtype="uint8")
cv2.imshow("Red", cv2.merge([zeros, zeros, R]))
cv2.imshow("Green", cv2.merge([zeros, G, zeros]))
cv2.imshow("Blue", cv2.merge([B, zeros, zeros]))

cv2.waitKey(0)

