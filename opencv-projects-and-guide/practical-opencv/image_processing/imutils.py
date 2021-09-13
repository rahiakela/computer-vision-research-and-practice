# Import the necessary packages
import numpy as np
import cv2


def translate(image, x, y):
    """
    Translation is the shifting of an image along the x and y
    axis. Using translation, we can shift an image up, down,
    left, or right, along with any combination of the above!
    """
    M = np.float32([
        [1, 0, x],  # [1, 0, Tx] for shifting left or right
        [0, 1, y]   # [1, 0, Ty] for shifting up or down
    ])
    shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

    return shifted


def rotate(image, angle, center=None, scale=1.0):
    """
    Rotation is exactly what it sounds like: rotating an image by some angle theta.
    We’ll use theta to represent by how many degrees we are rotating the image.
    """

    # grabs the width and height of the image
    (h, w) = image.shape[:2]

    if center is None:
        # divides width and height by 2 to determine the center
        center = (w // 2, h // 2)
    # rotate the image theta degrees and scale of the image
    M = cv2.getRotationMatrix2D(center, angle, scale)
    # apply the rotation to the image
    rotated = cv2.warpAffine(image, M, (w, h))

    return rotated


def resize(image, width=None, height=None, inter=cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image

    # resize the image by specifying the height
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:  # resize the image by specifying the width
        r = width / float(w)
        dim = (width, int(h * r))

    resized = cv2.resize(image, dim, interpolation=inter)

    return resized


