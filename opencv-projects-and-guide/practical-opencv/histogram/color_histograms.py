from matplotlib import pyplot as plt
import cv2
import numpy as np
import config


img = cv2.imread(config.GLOBAL_IMG_PATH + "beach.png")
cv2.imshow("Original", img)

# split the image into its three channels
channels = cv2.split(img)
colors = ("b", "g", "r")

# plot histogram
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")

for (ch, color) in zip(channels, colors):
    # computes the actual histogram
    hist = cv2.calcHist([ch], [0], None, [256], [0, 256])
    plt.plot(hist, color=color)
    plt.xlim([0, 256])
plt.show()

fig = plt.figure()

ax = fig.add_subplot(131)
hist = cv2.calcHist([channels[1], channels[0]], [0, 1], None, [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation="nearest")
ax.set_title("2D Color Histogram for G and B")
plt.colorbar(p)

ax = fig.add_subplot(132)
hist = cv2.calcHist([channels[1], channels[2]], [0, 1], None, [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation="nearest")
ax.set_title("2D Color Histogram for G and R")
plt.colorbar(p)

ax = fig.add_subplot(133)
hist = cv2.calcHist([channels[0], channels[2]], [0, 1], None, [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation="nearest")
ax.set_title("2D Color Histogram for B and R")
plt.colorbar(p)

print(f"2D histogram shape: {hist.shape}, with {hist.flatten().shape[0]} values")

"""
We are now computing an 8 X 8 X 8 histogram for each of the RGB channels. 
We can’t visualize this histogram, but we can see that the shape is indeed (8,8,8) with 512 values.
"""
hist = cv2.calcHist([img], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])

plt.show()
print(f"3D histogram shape: {hist.shape}, with {hist.flatten().shape[0]} values")

cv2.waitKey(0)
