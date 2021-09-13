import cv2
import numpy as np
import config

# loading webcam
cap = cv2.VideoCapture(0)
img_target = cv2.imread(config.GLOBAL_IMG_PATH + "sapiens1.jpeg")
my_video = cv2.VideoCapture(config.GLOBAL_VIDEO_PATH + "sample.mpg")

success, img_vid = my_video.read()

# get image h, w, c
h_t, w_t, c_t = img_target.shape
img_video = cv2.resize(img_vid, (w_t, h_t))

orb = cv2.ORB_create(nfeatures=1000)
keypoint1, desc1 = orb.detectAndCompute(img_target, None)
# img_target = cv2.drawKeypoints(img_target, keypoint1, None)

while True:
    success, img_webcam = cap.read()
    keypoint2, desc2 = orb.detectAndCompute(img_webcam, None)
    # img_webcam = cv2.drawKeypoints(img_webcam, keypoint2, None)

    bf_matcher = cv2.BFMatcher()
    matches = bf_matcher.knnMatch(desc1, desc2, k=2)
    good = []
    for m, n in matches:
        if m.distance < 0.75 * n.distance:
            good.append(m)
    print(len(good))
    img_features = cv2.drawMatches(img_target, keypoint1, img_webcam, keypoint2, good, None, flags=2)

    cv2.imshow("Image features", img_features)
    cv2.imshow("Target video", img_video)
    cv2.imshow("Webcam", img_webcam)

    cv2.waitKey(0)

