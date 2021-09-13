import cv2

frame_width = 640
frame_height = 480

cap = cv2.VideoCapture(0)
cap.set(3, frame_width)
cap.set(4, frame_height)
cap.set(10, 150)

while True:
    success, img = cap.read()
    cv2.imshow("Result", img)

    if cv2.waitKey(1) and 0xFF == ord("q"):
        break
