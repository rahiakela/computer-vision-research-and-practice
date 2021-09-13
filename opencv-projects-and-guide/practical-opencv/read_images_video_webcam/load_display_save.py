import cv2

img = cv2.imread("D:\\ml-datasets\\open-cv-dataset\\images\\trex.png")
cv2.imshow("Tyrannosaurus Rex", img)

print(f"height: {img.shape[0]} pixels")
print(f"width: {img.shape[1]} pixels")
print(f"channels: {img.shape[2]}")

# write image to file in JPG format
cv2.imwrite("newimage.jpg", img)

cv2.waitKey(0)