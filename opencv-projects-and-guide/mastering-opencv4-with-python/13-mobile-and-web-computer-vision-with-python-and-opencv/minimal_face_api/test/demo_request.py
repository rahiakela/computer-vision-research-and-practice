import requests

FACE_DETECTION_REST_API_URL = "http://localhost:5000/detect"
FACE_DETECTION_REST_API_URL_WRONG = "http://localhost:5000/process"
IMAGE_PATH = "images/test_two_faces.jpeg"
URL_IMAGE = "https://raw.githubusercontent.com/opencv/opencv/master/samples/data/lena.jpg"

# Submit the GET request
response = requests.get(FACE_DETECTION_REST_API_URL_WRONG)
# See the response
print("status code: {}".format(response.status_code))
print("headers: {}".format(response.headers))
print("content: {}".format(response.text))

# Submit the GET request
payload = {"url": URL_IMAGE}
response = requests.get(FACE_DETECTION_REST_API_URL, params=payload)
print("status code: {}".format(response.status_code))
print("headers: {}".format(response.headers))
print("content: {}".format(response.json()))

# Submit the GET request
response = requests.get(FACE_DETECTION_REST_API_URL)
print("status code: {}".format(response.status_code))
print("headers: {}".format(response.headers))
print("content: {}".format(response.json()))

# Load the image and construct the payload:
image = open(IMAGE_PATH, "rb").read()
payload = {"image": image}

response = requests.post(FACE_DETECTION_REST_API_URL, files=payload)
print("status code: {}".format(response.status_code))
print("headers: {}".format(response.headers))
print("content: {}".format(response.json()))

# Submit the PUT request
response = requests.put(FACE_DETECTION_REST_API_URL, files=payload)
print("status code: {}".format(response.status_code))
print("headers: {}".format(response.headers))
print("content: {}".format(response.json()))
