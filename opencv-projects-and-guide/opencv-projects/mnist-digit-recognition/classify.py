import joblib
from hog import HOG
import dataset
import mahotas
import cv2
import config


# load the trained model
model = joblib.load("models/svm.cpickle")

# instantiates HOG descriptor
hog = HOG(orientations=18, pixels_per_cell=(10, 10), cells_per_block=(1, 1), transform=True)

# classify the digits in the image
# image = cv2.imread(config.GLOBAL_IMG_PATH + "cellphone.png")
# image = cv2.imread(config.GLOBAL_IMG_PATH + "apple_phonenumber.png")
image = cv2.imread(config.GLOBAL_IMG_PATH + "digit_sample.png")
# image = cv2.imread(config.GLOBAL_IMG_PATH + "umbc_zipcode.png")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# apply Gaussian blurring
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
# apply Canny edge detector
edged = cv2.Canny(blurred, 30, 150)

# finds contours in the edged image and sorts them from left to right
(cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = sorted([(c, cv2.boundingRect(c)[0]) for c in cnts], key=lambda x: x[1])

# now needs to process each of these digits
for (c, _) in cnts:
    # compute bounding box for each contour
    (x, y, w, h) = cv2.boundingRect(c)

    if w >= 7 and h >= 20:
        # extract Region of Interest (ROI)
        roi = gray[y: y + h, x: x + w]
        thresh = roi.copy()
        # apply Otsu’s thresholding method to segment the foreground from the background
        T = mahotas.thresholding.otsu(roi)
        thresh[thresh > T] = 255
        thresh = cv2.bitwise_not(thresh)

        # deskew and translate to the center of the image
        thresh = dataset.deskew(thresh, 20)
        thresh = dataset.center_extent(thresh, (20, 20))

        # cv2.imshow("thresh", thresh)

        # extract features from the image and classify it
        hist = hog.describe(thresh)
        digit = model.predict([hist])[0]
        print("I think that number is: {}".format(digit))

        # draw a rectangle around the digit, the show what the digit was classified as
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 1)
        cv2.putText(image, str(digit), (x - 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 2)

        cv2.imshow("image", image)
        cv2.waitKey(0)
