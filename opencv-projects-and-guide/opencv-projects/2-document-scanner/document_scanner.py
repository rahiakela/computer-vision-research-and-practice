import cv2
import numpy as np

img_width = 640
img_height = 480

cap = cv2.VideoCapture(0)
cap.set(3, img_width)
cap.set(4, img_height)
cap.set(10, 150)


def preprocessing(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_blurred = cv2.GaussianBlur(img_gray, (5, 5), 1)
    img_canny = cv2.Canny(img_blurred, 200, 200)
    kernel = np.ones((5, 5))
    img_dilated = cv2.dilate(img_canny, kernel, iterations=2)
    img_thres = cv2.erode(img_dilated, kernel, iterations=2)

    return img_thres


def get_contours(img):
    biggest = np.array([])
    max_area = 0
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 5000:
            # cv2.drawContours(img_contour, cnt, -1, (255, 0, 0), 3)
            perimeter = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * perimeter, True)
            if area > max_area and len(approx) == 4:
                biggest = approx
                max_area = area
    cv2.drawContours(img_contour, biggest, -1, (255, 0, 0), 20)
    return biggest


def reorder(points):
    # my_points = np.ones((4, 2))
    my_points = points.reshape((4, 2))
    my_points_new = np.zeros((4, 1, 2), np.int32)
    add = my_points.sum(1)
    # print("add", add)

    my_points_new[0] = my_points[np.argmin(add)]
    my_points_new[3] = my_points[np.argmax(add)]

    diff = np.diff(my_points, axis=1)
    my_points_new[1] = my_points[np.argmin(diff)]
    my_points_new[2] = my_points[np.argmax(diff)]
    # print("NewPoints ", my_points_new)

    return my_points_new


def get_warp(img, biggest):
    biggest = reorder(biggest)
    pts1 = np.float32(biggest)
    pts2 = np.float32([[0, 0], [img_width, 0], [0, img_height], [img_width, img_height]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    img_output = cv2.warpPerspective(img, matrix, (img_width, img_height))

    return img_output


while True:
    success, img = cap.read()
    img = cv2.resize(img, (img_width, img_height))
    img_contour = img.copy()

    img_thres = preprocessing(img)
    biggest = get_contours(img_thres)
    print(biggest)

    img_warped = get_warp(img, biggest)

    cv2.imshow("Result", img_warped)

    if cv2.waitKey(1) and 0xFF == ord("q"):
        break
