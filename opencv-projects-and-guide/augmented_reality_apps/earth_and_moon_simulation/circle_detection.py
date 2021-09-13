import cv2
import numpy as np

capture = cv2.VideoCapture(0)

# threshold for Canny Edge Detection algorithm
T = 100
W = 640

while True:
    # reading camera image
    ret, img = capture.read()

    #  resize the image
    img_height, img_width, _ = img.shape
    scale = W // img_width
    H = img_height * scale
    img = cv2.resize(img, (0, 0), fx=scale, fy=scale)

    """
    Then we want to convert it to a gray-scaled image and apply first median blur 
    which removes noise and retains edges, and then the Canny edge detector to see 
    what the circle detection algorithm is going to work with.
    """
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.medianBlur(gray, 15)

    # Create 2x2 grid for all previews
    grid = np.zeros([2 * H, 2 * W, 3], np.uint8)
    grid[0: H, 0: W] = img

    # We need to convert each of them to RGB from gray-scaled 8 bit format
    grid[H: 2 * H, 0: W] = np.dstack([cv2.Canny(gray, T // 2, T)] * 3)
    grid[0: H, W: 2 * W] = np.dstack([blurred] * 3)
    grid[H: 2 * H, W: 2 * W] = np.dstack([cv2.Canny(blurred, T // 2, T)] * 3)

    cv2.imshow("Image previews", grid)

    # detection the actual circle
    scale = 1      # Scale for the algorithm
    min_dist = 30  # Minimum required distance between two circles
    at = 40        # Accumulator threshold for circle detection
    circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, scale, min_dist, T, at)
    if circles is not None:
        # We care only about the first circle found
        # circles = np.round(circles[0, :]).astype("int")
        circle = circles[0][0]
        x, y, radius = int(circle[0]), int(circle[1]), int(circle[2])
        print(x, y, radius)

        # Highlight the circle
        cv2.circle(img, (x, y), radius, (0, 0, 255), 1)
        # Draw dot in the center
        cv2.circle(img, (x, y), 1, (0, 0, 255), 1)

    cv2.imshow("Image with detected circle", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
