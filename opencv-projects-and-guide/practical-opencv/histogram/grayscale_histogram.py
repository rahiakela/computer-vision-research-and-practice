from matplotlib import pyplot as plt
import cv2
import config


img = cv2.imread(config.GLOBAL_IMG_PATH + "beach.png")
cv2.imshow("Original", img)

# computes the actual histogram
hist = cv2.calcHist([img], [0], None, [256], [0, 256])

# plot histogram
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(hist)
plt.xlim([0, 256])
plt.show()

cv2.waitKey(0)
