import cv2
import numpy as np
import config
import imutils
from face_detector import FaceDetector


# construct the face detector
face_detector = FaceDetector(config.GLOBAL_CASCADE_PATH + "haarcascade_frontalface_default.xml")

# load the video
camera = cv2.VideoCapture(config.GLOBAL_VIDEO_PATH + "adrian_face.mov")

# keep looping
while True:
    # grab the current frame
    (grabbed, frame) = camera.read()
    # resize the frame and convert it to grayscale
    frame = imutils.resize(frame, width=300)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # detect faces in the image and then clone the frame so that we can draw on it
    face_rects = face_detector.detect(gray, scale_factor=1.1, min_neighbors=5, min_size=(30, 30))
    frame_clone = frame.copy()

    # loop over the face bounding boxes and draw them
    for (fx, fy, fw, fh) in face_rects:
        cv2.rectangle(frame_clone, (fx, fy), (fx + fw, fy + fh), (0, 255, 0), 2)

    # show our detected faces
    cv2.imshow("Face", frame_clone)

    # if the 'q' key is pressed, stop the loop
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# cleanup the camera and close any open windows
camera.release()
cv2.destroyAllWindows()
