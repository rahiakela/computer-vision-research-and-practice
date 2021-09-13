import cv2
import numpy as np
import config

####################################################
img_width = 640
img_height = 480
min_area = 500
color = (255, 255, 255)
number_plates_cascade = cv2.CascadeClassifier(config.GLOBAL_CASCADE_PATH + "haarcascade_indian_license_plate.xml")
####################################################

cap = cv2.VideoCapture(0)
cap.set(3, img_width)
cap.set(4, img_height)
cap.set(10, 150)

while True:
    success, img1 = cap.read()
    img = cv2.imread(config.GLOBAL_IMG_PATH + "cars1.jpg")
    # convert image to grayscale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # detect number plates in image
    number_plates = number_plates_cascade.detectMultiScale(img_gray, 1.1, 4)

    # create bounding box around number plates
    for (x, y, w, h) in number_plates:
        area = w * h
        if area > min_area:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(img, "Number Plate",
                        (x, y - 5),
                        cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, color, 2)
            img_roi = img[y: y + h, x: x + w]  # region of number plates
            cv2.imshow("ROI", img_roi)

    cv2.imshow("Result", img)

    if cv2.waitKey(1) and 0xFF == ord("q"):
        break
