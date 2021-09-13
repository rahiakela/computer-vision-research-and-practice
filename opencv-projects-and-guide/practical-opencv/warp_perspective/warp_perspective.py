import cv2
import numpy as np
import config

img = cv2.imread(config.GLOBAL_IMG_PATH + "cards.jpg")
cv2.imshow("Original", img)
cv2.waitKey(0)

width, height = 250, 350
point1 = np.float32([
    [111, 219], [287, 188], [154, 482], [352, 440]
])
point2 = np.float32([
    [0, 0], [width, 0], [0, height], [width, height]
])

matrix = cv2.getPerspectiveTransform(point1, point2)
img_output = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("Warp Image", img_output)
cv2.imwrite("king_pan.jpg", img_output)
cv2.waitKey(0)

point1 = np.float32([
    [279, 119], [445, 130], [272, 345], [450, 360]
])

matrix = cv2.getPerspectiveTransform(point1, point2)
img_output = cv2.warpPerspective(img, matrix, (width, height))
cv2.imshow("Warp Image", img_output)
cv2.waitKey(0)
