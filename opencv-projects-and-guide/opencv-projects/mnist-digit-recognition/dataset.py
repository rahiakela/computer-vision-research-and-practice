import imutils
import numpy as np
import mahotas
import cv2


def load_digits(dataset_path):
    # loads the dataset off disk and stores it as an unsigned 8-bit NumPy array.
    data = np.genfromtxt(dataset_path, delimiter=",", dtype="uint8")
    # get target
    target = data[:, 0]
    # reshape feature
    data = data[:, 1:].reshape(data.shape[0], 28, 28)

    return data, target


def deskew(image, width):
    """In order to help fix some of the “lean” of digits"""

    # grabs the height and width of the image
    (h, w) = image.shape[:2]
    # compute the moments of the image
    moments = cv2.moments(image)

    # compute the skew based on the moments
    skew = moments["mu11"] / moments["mu02"]
    # construct the warping matrix that will be used to deskew the image
    M = np.float32([
        [1, skew, -0.5 * w * skew],
        [0, 1, 0]
    ])
    # do the actual deskewing of the image
    image = cv2.warpAffine(image, M, (w, h), flags=cv2.WARP_INVERSE_MAP | cv2.INTER_AREA)
    image = imutils.resize(image, width=width)

    return image


def center_extent(image, size):
    """
    In order to obtain a consistent representation of digits
    where all images are of the same width and height, with
    the digit placed at the center of the image, then needs
    to define the extent of an image:
    """
    (eW, eH) = size

    # resize the image based on its width if the width is greater than the height of the image
    if image.shape[1] > image.shape[0]:
        image = imutils.resize(image, width=eW)
    else:  # resize the image based on its height if the height is greater than the width of the image
        image = imutils.resize(image, height=eH)

    # allocates spaces on the extent of the image
    extent = np.zeros((eH, eW), dtype="uint8")
    offsetX = (eW - image.shape[1]) // 2
    offsetY = (eH - image.shape[0]) // 2
    # The actual extent is set using array slicing
    extent[offsetY: offsetX + image.shape[0], offsetX: offsetX + image.shape[1]] = image

    # computes the weighted mean of the white pixels in the image
    CM = mahotas.center_of_mass(extent)
    (cY, cX) = np.round(CM).astype("int32")
    # translate the digit so it is placed at the center of the image
    (dX, dY) = ((size[0] // 2) - cX, (size[1] // 2) - cY)
    M = np.float32([
        [1, 0, dX],
        [0, 1, dY]
    ])
    extent = cv2.warpAffine(extent, M, size)

    return extent

