import numpy as np
import cv2

"""
Bitwise operations operate in a binary manner and are
represented as grayscale images. A given pixel is turned
“off” if it has a value of zero, and it is turned “on” if the
pixel has a value greater than zero.
"""
rectangle = np.zeros((300, 300), dtype="uint8")
cv2.rectangle(rectangle, (25, 25), (275, 275), 255, -1)
cv2.imshow("Rectangle", rectangle)

circle = np.zeros((300, 300), dtype="uint8")
cv2.circle(circle, (150, 150), 150, 255, -1)
cv2.imshow("Circle", circle)

bitwiseAnd = cv2.bitwise_and(rectangle, circle)
cv2.imshow("AND", bitwiseAnd)

bitwiseOr = cv2.bitwise_or(rectangle, circle)
cv2.imshow("OR", bitwiseOr)

bitwiseXOR = cv2.bitwise_xor(rectangle, circle)
cv2.imshow("XOR", bitwiseXOR)

bitwiseNot = cv2.bitwise_not(rectangle, circle)
cv2.imshow("NOT", bitwiseNot)

cv2.waitKey(0)
