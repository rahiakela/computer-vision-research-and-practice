import cv2
import config

# LOAD AN IMAGE USING 'IMREAD'
img = cv2.imread(config.GLOBAL_IMG_PATH + "lena.png")
# DISPLAY
cv2.imshow("Lena Soderberg", img)
cv2.waitKey(0)