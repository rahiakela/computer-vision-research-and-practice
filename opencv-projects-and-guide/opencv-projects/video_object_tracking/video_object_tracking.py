import cv2
import numpy as np
import config
import time


# define the upper and lower boundaries for a color to be considered "blue"
blueLower = np.array([100, 67, 0], dtype="uint8")
blueUpper = np.array([255, 128, 50], dtype = "uint8")

# load the video
camera = cv2.VideoCapture(config.GLOBAL_VIDEO_PATH + "iphonecase.mov")

# keep looping
while True:
    # grab the current frame
    (grabbed, frame) = camera.read()

    # check to see if we have reached the end of the video
    if not grabbed:
        break

    # determine which pixels fall within the blue boundaries and then blur the binary image
    blue_thresholded = cv2.inRange(frame, blueLower, blueUpper)
    blurred = cv2.GaussianBlur(blue_thresholded, (3, 3), 0)

    # finds the contours in the thresholded image
    (cnts, _) = cv2.findContours(blurred.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # check to see if any contours were found
    if len(cnts) > 0:
        # sort the contours and find the largest one
        # we will assume this contour correspondes to the area of my phone
        cnt = sorted(cnts, key=cv2.contourArea, reverse=True)[0]

        # compute the (rotated) bounding box around then contour and then draw it
        rect = np.int32(cv2.boxPoints(cv2.minAreaRect(cnt)))
        cv2.drawContours(frame, [rect], -1, (0, 255, 0), 2)

    # show the frame and the binary image
    cv2.imshow("Tracking", frame)
    cv2.imshow("Binary", blurred)

    # if your machine is fast, it may display the frames in
    # what appears to be 'fast forward' since more than 32
    # frames per second are being displayed -- a simple hack
    # is just to sleep for a tiny bit in between frames;
    # however, if your computer is slow, you probably want to
    # comment out this line
    time.sleep(0.025)

    # if the 'q' key is pressed, stop the loop
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# cleanup the camera and close any open windows
camera.release()
cv2.destroyAllWindows()

