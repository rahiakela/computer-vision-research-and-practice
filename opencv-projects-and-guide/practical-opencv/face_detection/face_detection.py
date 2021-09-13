import cv2
import config

img = cv2.imread(config.GLOBAL_IMG_PATH + "ryaan-arhaan.jpeg")

face_cascade = cv2.CascadeClassifier(config.GLOBAL_CASCADE_PATH + "haarcascade_frontalface_default.xml")

# convert image to grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# detect face in image
faces = face_cascade.detectMultiScale(img_gray, 1.1, 4)

# create bounding box around face
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), )
    cv2.putText(img, "Face",
                (x, y-5),
                cv2.FONT_HERSHEY_COMPLEX, 0.5,
                (255, 255, 255), 2)

img = cv2.resize(img, (1260, 940))
cv2.imshow("Result", img)

cv2.waitKey(0)
