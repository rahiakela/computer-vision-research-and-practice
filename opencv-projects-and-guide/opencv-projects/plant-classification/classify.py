from __future__ import print_function
from rgbhistogram import RGBHistogram
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
import numpy as np
import glob
import cv2


PLANT_DATASET = "D:\\ml-datasets\\plant-dataset"

# grab the image and mask paths
image_paths = sorted(glob.glob(PLANT_DATASET + "\\images\\*.png"))
mask_paths = sorted(glob.glob(PLANT_DATASET + "\\masks\\*.png"))

# initialize the list of data and class label targets
data = []
target = []

# initialize the image descriptor
img_descriptor = RGBHistogram([8, 8, 8])

# loop over the image and mask paths
for (img_path, mask_path) in zip(image_paths, mask_paths):
    # load the image and mask
    image = cv2.imread(img_path)
    mask = cv2.imread(mask_path)

    # converts the mask to grayscale
    mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)

    # describe the image
    features = img_descriptor.describe(image, mask)

    # update the list of data and targets
    data.append(features)
    target.append(img_path.split("_")[-2])

# grab the unique target names and encode the labels
target_names = np.unique(target)
label_encoder = LabelEncoder()
target = label_encoder.fit_transform(target)

# construct the training and testing splits
(train_data, test_data, train_target, test_target) = train_test_split(data,
                                                                      target,
                                                                      test_size=0.3,
                                                                      random_state=2021)

# train the classifier
model = RandomForestClassifier(n_estimators=25, random_state=2020)
model.fit(train_data, train_target)

# evaluate the classifier
print(classification_report(test_target,
                            model.predict(test_data),
                            target_names=target_names))

# loop over a sample of the images
for i in np.random.choice(np.arange(0, len(image_paths)), 10):
    # grab the image and mask paths
    image_path = image_paths[i]
    mask_path = mask_paths[i]

    # load the image and mask
    image = cv2.imread(image_path)
    mask = cv2.imread(mask_path)

    # converts the mask to grayscale
    mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)

    # describe the image
    features = img_descriptor.describe(image, mask)

    # predict what type of flower the image is
    flower = label_encoder.inverse_transform(model.predict([features]))[0]
    print(image_path)
    print("I think this flower is a {}".format(flower.upper()))

    cv2.imshow("image", image)
    cv2.waitKey(0)
