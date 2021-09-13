from sklearn.svm import LinearSVC
import joblib
from hog import HOG
import dataset


# load the dataset consisting of the images and targets
(digits, target) = dataset.load_digits("D:\\ml-datasets\\mnist\\train.csv")
data = []

# instantiates HOG descriptor
hog = HOG(orientations=18, pixels_per_cell=(10, 10), cells_per_block=(1, 1), transform=True)

# loop over digit images
for image in digits:
    image = dataset.deskew(image, 20)               # deskew the image
    image = dataset.center_extent(image, (20, 20))  # translate to the center of the image

    # compute the HOG feature vector
    hist = hog.describe(image)
    data.append(hist)


# now ready to train model
model = LinearSVC(random_state=42)
model.fit(data, target)

# dumps the model to disk for later use
joblib.dump(model, "models/svm.cpickle")
