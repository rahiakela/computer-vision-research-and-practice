import numpy as np
import cv2


class CoverDescriptor:

    def __init__(self, SIFT=False):
        self.SIFT = SIFT

    def describe(self, image):
        descriptor = cv2.BRISK_create()
        if self.SIFT:
            descriptor = cv2.xfeatures2d.SIFT_create()
        # detects keypoints and then describes and quantifies the region surrounding each of the keypoints
        (kps, descs) = descriptor.detectAndCompute(image, None)
        # stores the points as a NumPy array
        kps = np.float32([kp.pt for kp in kps])

        return (kps, descs)

