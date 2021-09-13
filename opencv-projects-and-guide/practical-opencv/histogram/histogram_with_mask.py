import numpy as np
from matplotlib import pyplot as plt
import cv2
import config


"""
Histogram equalization is normally useful when enhancing the contrast of
medical or satellite images and an X-ray.

Masks can be used to focus on specific regions of an image that interest
us. We are now going to construct a mask and compute
color histograms for the masked region only.
"""

img = cv2.imread(config.GLOBAL_IMG_PATH + "beach.png")
cv2.imshow("Original", img)


def plot_histogram(image, title, mask=None):
    chans = cv2.split(image)
    colors = ("b", "g", "r")
    plt.figure()
    plt.title(title)
    plt.xlabel("Bins")
    plt.ylabel("# of Pixels")

    for (chan, color) in zip(chans, colors):
        hist = cv2.calcHist([chan], [0], mask, [256], [0, 256])
        plt.plot(hist, color=color)
        plt.xlim([0, 256])


plot_histogram(img, "Histogram for Original Image")

# compute a histogram for the masked region
mask = np.zeros(img.shape[:2], dtype="uint8")
cv2.rectangle(mask, (15, 15), (130, 100), 255, -1)
cv2.imshow("Mask", mask)

masked = cv2.bitwise_and(img, img, mask=mask)
cv2.imshow("Applying the Mask", masked)

plot_histogram(img, "Histogram for Masked Image", mask=mask)
plt.show()

cv2.waitKey(0)
