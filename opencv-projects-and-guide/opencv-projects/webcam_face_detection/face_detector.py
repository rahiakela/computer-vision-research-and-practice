import cv2


class FaceDetector:

    def __init__(self, face_cascade_path):
        self.face_cascade = cv2.CascadeClassifier(face_cascade_path)

    def detect(self, image, scale_factor=1.1, min_neighbors=5, min_size=(30, 30)):
        rects = self.face_cascade.detectMultiScale(image,
                                                   scaleFactor=scale_factor,
                                                   minNeighbors=min_neighbors,
                                                   minSize=min_size,
                                                   flags=cv2.CASCADE_SCALE_IMAGE)
        return rects

