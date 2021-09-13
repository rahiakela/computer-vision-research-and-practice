"""
I have build Flask REST API for Tensorflow 2 pre-trained model

Reference: https://blog.keras.io/
"""
from tensorflow.keras.applications import nasnet, NASNetMobile
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications import imagenet_utils

from PIL import Image
import numpy as np
from flask import Flask, jsonify, request
import io


# Initialize Flask app, Keras model and graph
app = Flask(__name__)
model = None


def load_model():
    # Load the pre-trained Keras model(pre-trained on ImageNet)
    global model
    model = NASNetMobile(weights="imagenet")


def preprocessing_image(image, target):
    # Make sure the image mode is RGB
    if image.mode != "RGB":
        image = image.convert("RGB")
    # Resize the input image
    image = image.resize(target)
    # Convert PIL format to numpy array
    image = img_to_array(image)
    # Convert the image/images into batch format
    image = np.expand_dims(image, axis=0)
    # Pre-process (prepare) the image using the specific architecture
    image = nasnet.preprocess_input(image)

    return image


@app.route("/predict", methods=["POST"])
def predict():
    # Initialize result
    result = {"success": False}

    if request.method == "POST":
        if request.files.get("image"):
            # Read input image in PIL format
            image = request.files["image"].read()
            image = Image.open(io.BytesIO(image))

            # Pre-process the image to be classified
            image = preprocessing_image(image, target=(224, 224))

            # Classify the input image
            predictions = model.predict(image)
            results = imagenet_utils.decode_predictions(predictions)

            result["predictions"] = []
            # Add the predictions to the result
            for (imagenet_id, label, prob) in results[0]:
                r = {"label": label, "probability": float(prob)}
                result["predictions"].append(r)
            # At this point we can say that the request was dispatched successfully
            result["success"] = True

    # Return result as a JSON response
    return jsonify(result)


@app.route("/")
def home():
    # Initialize result
    result = {"success": False}
    # Return result as a JSON response
    return jsonify(result)


if __name__ == '__main__':
    print("Loading Keras pre-trained model............")
    load_model()
    print("Starting.............")
    app.run(host="0.0.0.0")
