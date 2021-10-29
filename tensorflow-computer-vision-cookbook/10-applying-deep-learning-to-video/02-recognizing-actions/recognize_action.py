import os
import random
import re
import ssl
import tempfile
from urllib import request

import cv2
import imageio
import numpy as np
import tensorflow as tf
import tensorflow_hub as tfhub

"""
Define the path to the UCF101 – Action Recognition dataset, 
from where we'll fetch the test videos that we will pass to the model
"""
UCF_ROOT = "https://www.crcv.ucf.edu/THUMOS14/UCF101/UCF101/"
# Define the path to the labels file of the Kinetics dataset, the one used to train the 3D convolutional network
KINETICS_URL = ("https://raw.githubusercontent.com/deepmind/", "kinetics-i3d/master/data/label_map.txt")

# Create a temporary directory to cache the downloaded resources
CACHE_DIR = tempfile.mkdtemp()

# Create an unverified SSL context. We need this to be able to download data from UCF's site
UNVERIFIED_CONTEXT = ssl._create_unverified_context()


def fetch_ucf_videos():
    """
    This function downloads the list of the possible videos we'll choose from to test our action recognizer
    """
    index = (request.urlopen(UCF_ROOT, context=UNVERIFIED_CONTEXT).read().decode('utf-8'))
    videos = re.findall("(v_[\w]+\.avi)", index)

    return sorted(videos)


def fetch_kinetics_labels():
    """
    This function is used to download and parse the labels of the Kinetics dataset
    """
    with request.urlopen(KINETICS_URL) as f:
        labels = [line.decode("utf-8").strip() for line in f.readlines()]
    return labels


def fetch_random_video(videos_list):
    """
    This function selects a random video from our list of UCF101 videos and downloads it to the temporary directory
    """
    video_name = random.choice(videos_list)
    cache_path = os.path.join(CACHE_DIR, video_name)

    if not os.path.exists(cache_path):
        url = request.urlopen(UCF_ROOT, video_name)

        response = (request.urlopen(url, context=UNVERIFIED_CONTEXT).read())
        with open(cache_path, "wb") as f:
            f.write(response)

    return cache_path


def crop_center(frame):
    """
    This function takes an image and crops a squared selection corresponding to the center of the received frame
    """
    height, width = frame.shape[:2]
    smallest_dimension = min(height, width)

    x_start = (width // 2) - (smallest_dimension // 2)
    x_end = x_start + smallest_dimension

    y_start = (height // 2) - (smallest_dimension // 2)
    y_end = y_start + smallest_dimension

    roi = frame[y_start: y_end, x_start: x_end]

    return roi


def read_video(path, max_frames=32, resize=(224, 224)):
    """
    This function reads up to max_frames from a video stored in our cache and
    returns a list of all the read frames. It also crops the center of each frame,
    resizes it to 224x224x3 (the input shape expected by the network), and normalizes it
    """
    capture = cv2.VideoCapture(path)

    frames = []
    while len(frames) <= max_frames:
        frame_read, frame = capture.read()

        if not frame_read:
            break

        frame = crop_center(frame)
        frame = cv2.resize(frame, resize)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frames.append(frame)

    capture.release()

    frames = np.array(frames)

    return frames // 255.


def predict(model, labels, sample_video):
    """
    This function is used to get the top five most likely actions recognized by the model in the input video
    """
    model_input = tf.constant(sample_video, dtype=tf.float32)
    model_input = model_input[tf.newaxis, ...]

    logits = model(model_input)["default"][0]
    probabilities = tf.nn.softmax(logits)

    print("Top 5 actions:")
    for i in np.argsort(probabilities)[::-1][:5]:
        print(f"{labels[i]}: {probabilities[i] * 100:5.2f}%")


def save_as_gif(images, video_name):
    """
    This function will takes a list of frames corresponding to a video, and uses them to create a GIF representation
    """
    converted_images = np.clip(images * 255, 0, 255)
    converted_images = converted_images.astype(np.uint8)

    imageio.mimsave(f"./{video_name}.gif", converted_images, fps=25)


# Fetch the videos and labels
VIDEO_LIST = fetch_ucf_videos()
LABELS = fetch_kinetics_labels()

# Fetch a random video and read its frames
video_path = fetch_random_video(VIDEO_LIST)
sample_video = read_video(video_path)

# Load the I3D from TFHub
model_path = "https://tfhub.dev/deepmind/i3d-kinetics-400/1"
model = tfhub.load(model_path)
model = model.signatures["default"]

# Finally, pass the video through the network to obtain the predictions,
# and then save the video as a GIF
predict(model, LABELS, sample_video)
video_name = video_path.rsplit("/", maxsplit=1)[1][:-4]
save_as_gif(sample_video, video_name)