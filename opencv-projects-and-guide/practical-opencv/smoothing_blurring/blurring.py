import numpy as np
import cv2
import config


img = cv2.imread(config.GLOBAL_IMG_PATH + "beach.png")
cv2.imshow("Original", img)

# “horizontally stacks” three images into a row.
blurred = np.hstack([
    cv2.blur(img, (3, 3)),
    cv2.blur(img, (5, 5)),
    cv2.blur(img, (7, 7)),
    cv2.blur(img, (9, 9))
])
# cv2.imshow("Averaged", blurred)

"""
Gaussian blurring is similar to average blurring, but instead of
using a simple mean, we are now using a weighted mean,
where neighborhood pixels that are closer to the central
pixel contribute more “weight” to the average.
"""
gaussian = np.hstack([
    cv2.GaussianBlur(img, (3, 3), 0),
    cv2.GaussianBlur(img, (5, 5), 0),
    cv2.GaussianBlur(img, (7, 7), 0),
    cv2.GaussianBlur(img, (9, 9), 0)
])
# cv2.imshow("Gaussian", blurred)

"""
Median blurring is more effective at removing salt-and
pepper style noise from an image because each central pixel
is always replaced with a pixel intensity that exists in the image.
"""
median_blurred = np.hstack([
    cv2.medianBlur(img, 3),
    cv2.medianBlur(img, 5),
    cv2.medianBlur(img, 7),
])
# cv2.imshow("Median", median_blurred)

"""
Thus far, the intention of our blurring methods has been
to reduce noise and detail in an image; however, we tend to
lose edges in the image.
In order to reduce noise while still maintaining edges, we
can use bilateral blurring. Bilateral blurring accomplishes
this by introducing two Gaussian distributions.
"""
bilateral_blurred = np.hstack([
    cv2.bilateralFilter(img, 5, 21, 21),
    cv2.bilateralFilter(img, 7, 31, 31),
    cv2.bilateralFilter(img, 9, 41, 41),
])
cv2.imshow("Bilateral", bilateral_blurred)

cv2.waitKey(0)
