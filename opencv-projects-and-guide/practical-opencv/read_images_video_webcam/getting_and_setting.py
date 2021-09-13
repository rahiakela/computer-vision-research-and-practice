import cv2

img = cv2.imread("D:\\ml-datasets\\open-cv-dataset\\images\\trex.png")
# cv2.imshow("Tyrannosaurus Rex", img)

# get the pixels value
(b, g, r) = img[0, 0]
print(f"Pixel at (0, 0) - Red: {r}, Green: {g}, Blue: {b}")

# making it a pure red color
img[0, 0] = (0, 0, 255)
(b, g, r) = img[0, 0]
print(f"Pixel at (0, 0) - Red: {r}, Green: {g}, Blue: {b}")

# access larger rectangular portions of the image using slicing
corner = img[0: 100, 0: 100]     # grab a 100X100 pixel region of the image
cv2.imshow("Corner", corner)

# use array slices to change the color of a region of pixels.
img[0:100, 0:100] = (0, 255, 0)  # update grabbed section with pure green color
cv2.imshow("Updated", img)

cv2.waitKey(0)