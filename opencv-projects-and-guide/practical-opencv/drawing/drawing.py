import cv2
import numpy as np

# create canvas with 300 rows and 300 columns with 3 channels for RGB
canvas = np.zeros((300, 300, 3), dtype="uint8")

# draw a green line from point (0, 0) (the top-left corner of the image) to point (300, 300)
green = (0, 255, 0)
cv2.line(canvas, (0, 0), (300, 300), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# draw a red line from the top-right corner of the image to the bottom left with thickness 3 pixels
red = (0, 0, 255)
cv2.line(canvas, (300, 0), (0, 300), red, 3)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# drawing rectangle
cv2.rectangle(canvas, (10, 10), (60, 60), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

cv2.rectangle(canvas, (50, 200), (200, 225), red, 5)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

blue = (255, 0, 0)
cv2.rectangle(canvas, (200, 50), (225, 125), blue, -1)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

canvas = np.zeros((300, 300, 3), dtype="uint8")
(center_x, center_y) = (canvas.shape[1] // 2, canvas.shape[0] // 2)
white = (255, 255, 255)

for r in range(0, 175, 25):
    cv2.circle(canvas, (center_x, center_y), r, white)
cv2.imshow("Circle", canvas)
cv2.waitKey(0)

# draw 25 random circles
for r in range(0, 25):
    radius = np.random.randint(5, high=200)
    color = np.random.randint(0, high=256, size=(3, )).tolist()
    pt = np.random.randint(0, high=300, size=(2, ))
    cv2.circle(canvas, tuple(pt), radius, color, -1)
cv2.imshow("Circle", canvas)
cv2.waitKey(0)
