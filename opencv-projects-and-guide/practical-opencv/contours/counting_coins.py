"""
Now we are going to use these edges to help us find the
actual coins in the image and count them.

OpenCV provides methods to find “curves” in an image,
called contours. A contour is a curve of points, with no
gaps in the curve. Contours are extremely useful for such
things as shape approximation and analysis.
"""
import cv2
import config
import numpy as np


img = cv2.imread(config.GLOBAL_IMG_PATH + "coins.png")
# convert to gray
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# blur it using the Gaussian blurring method
img_blurred = cv2.GaussianBlur(img_gray, (5, 5), 0)
cv2.imshow("Blurred", img_blurred)

# applying the Canny edge detector using threshold 1 and threshold 2
img_canny = cv2.Canny(img_blurred, 30, 150)
cv2.imshow("Edges", img_canny)

# find the contours of the outlines
cnts, _ = cv2.findContours(img_canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
"""
Our contours cnts is simply a Python list. We can use
the len function on it to count the number of contours that were returned.
"""
print("I count {} coins in this image".format(len(cnts)))

img_coins = img.copy()
# By specifying a negative value of -1, we are indicating that we want to draw all of the contours.
cv2.drawContours(img_coins, cnts, -1, (0, 255, 0), 2)
cv2.imshow("Coins", img_coins)

# draw the first, second, and third contours, respectively
cv2.imshow("Coins 1", cv2.drawContours(img.copy(), cnts, 0, (0, 255, 0), 2))

cv2.imshow("Coins 2", cv2.drawContours(img.copy(), cnts, 1, (0, 255, 0), 2))

cv2.imshow("Coins 3", cv2.drawContours(img.copy(), cnts, 2, (0, 255, 0), 2))


# Let’s crop each individual coin from the image
for (i, c) in enumerate(cnts):
    (x, y, w, h) = cv2.boundingRect(c)
    print("Coin #{}".format(i + 1))
    coin = img[y: y + h, x: x + w]
    cv2.imshow("Coin", coin)

    mask = np.zeros(img.shape[:2], dtype="uint8")
    ((centerX, centerY), radius) = cv2.minEnclosingCircle(c)
    cv2.circle(mask, (int(centerX), int(centerY)), int(radius), 255, -1)
    mask = mask[y: y + h, x: x + w]
    cv2.imshow("Masked Coin", cv2.bitwise_and(coin, coin, mask=mask))

cv2.waitKey(0)
