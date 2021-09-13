import cv2
import numpy as np
from PIL import Image
import os
import config

# Path for face image database
face_path = "face-dataset"

# use recognizer, the LBPH (LOCAL BINARY PATTERNS HISTOGRAMS) Face Recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier(config.GLOBAL_CASCADE_PATH + "haarcascade_frontalface_default.xml")


# function to get the images and label data
def get_image_and_labels(path):
    image_paths = [os.path.join(path, f) for f in os.listdir(path)]

    face_samples = []
    ids = []
    for image_path in image_paths:
        pil_img = Image.open(image_path).convert("L")  # convert it to grayscale
        img_numpy = np.array(pil_img, "uint8")
        id = int(os.path.split(image_path)[-1].split(".")[1])
        faces = detector.detectMultiScale(img_numpy)
        for (x, y, w, h) in faces:
            face_samples.append(img_numpy[y: y + h, x: x + w])
            ids.append(id)
    return face_samples, ids


print("\n [INFO] Training faces. It will take a few seconds. Wait ...")
# Now, take all photos on directory:"dataset/",
# getting 2 arrays: "Ids" and "faces"
faces, ids = get_image_and_labels(config.GLOBAL_FACE_DATASET_PATH + face_path)

# With those arrays as input, we will "train our recognizer"
recognizer.train(faces, np.array(ids))

# Save the model into trainer/trainer.yml
recognizer.write(config.GLOBAL_FACE_DATASET_PATH + "face-trainer/trainer.yml")

print("\n [INFO] {0} faces trained. Exiting Program".format(len(np.unique(ids))))

