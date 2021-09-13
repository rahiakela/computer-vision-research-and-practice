import requests

KERAS_REST_API_URL = "http://localhost:5000/predict"
IMAGE_PATH = "car.jpg"

# Load the image and construct the payload
image = open(IMAGE_PATH, "rb").read()
payload = {"image": image}

# Submit the POST request
response = requests.post(KERAS_REST_API_URL, files=payload).json()

# show the results
if response["success"]:
    #  Iterate over the predictions and print them
    for (cls_index, result) in enumerate(response["predictions"]):
        print("{}. {}: {:.4f}".format(cls_index + 1, result["label"], result["probability"]))
else:
    print("Request failed")
