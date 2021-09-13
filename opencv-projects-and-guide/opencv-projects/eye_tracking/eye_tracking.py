import cv2
import config
import imutils
from eye_tracker import EyeTracker


eye_tracker = EyeTracker(config.GLOBAL_CASCADE_PATH + "haarcascade_frontalface_default.xml",
                         config.GLOBAL_CASCADE_PATH + "haarcascade_eye.xml")

# load the webcam
camera = cv2.VideoCapture(0)

# looping over the frames of the video
while True:
    (grabbed, frame) = camera.read()

    # resizes the image to have a width of 300 pixels
    frame = imutils.resize(frame, width=300)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # track eyes in the image
    rects = eye_tracker.track(gray)

    # looping over the bounding box rectangles and draws each of them
    for rect in rects:
        cv2.rectangle(frame, (rect[0], rect[1]), (rect[2], rect[3]), (0, 255, 0), 2)

    cv2.imshow("Tracking", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
