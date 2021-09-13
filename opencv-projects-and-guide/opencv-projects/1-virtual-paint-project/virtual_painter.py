import cv2
import numpy as np
from utils import get_contours, find_color, draw_on_canvas

frame_width = 640
frame_height = 480

cap = cv2.VideoCapture(0)
cap.set(3, frame_width)
cap.set(4, frame_height)
cap.set(10, 150)

my_colors = [
    [5, 107, 0, 19, 255, 255],
    [133, 56, 0, 159, 156, 255],
    [57, 76, 0, 100, 255, 255],
    # [90, 48, 0, 118, 255, 255]
]
my_color_values = [   # BGR
    [51, 153, 255],
    [255, 0, 255],
    [0, 255, 0]
]
my_points = []  # [x, y, color_id]

while True:
    success, img = cap.read()
    img_result = img.copy()
    new_points = find_color(img_result, my_colors, my_color_values)
    if len(new_points) != 0:
        for point in new_points:
            my_points.append(point)
    if len(my_points) != 0:
        draw_on_canvas(img_result, my_points, my_color_values)
    cv2.imshow("Result", img_result)

    if cv2.waitKey(1) and 0xFF == ord("q"):
        break
