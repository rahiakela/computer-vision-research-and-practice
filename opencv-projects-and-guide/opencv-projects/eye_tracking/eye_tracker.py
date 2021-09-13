import cv2


class EyeTracker:

    def __init__(self, face_cascade_path, eye_cascade_path):
        self.face_cascade = cv2.CascadeClassifier(face_cascade_path)
        self.eye_cascade = cv2.CascadeClassifier(eye_cascade_path)

    def track(self, image):
        face_rects = self.face_cascade.detectMultiScale(image,
                                                        scaleFactor=1.1,
                                                        minNeighbors=5,
                                                        minSize=(30, 30),
                                                        flags=cv2.CASCADE_SCALE_IMAGE)
        rects = []

        # looping over the x, y, width, and height location of the faces
        for (fx, fy, fw, fh) in face_rects:
            # extracts the face Region of Interest (ROI) from the image
            face_roi = image[fy: fy + fh, fx: fx + fw]
            rects.append((fx, fy, fx + fw, fy + fh))

            # fetch list of locations in the image where eyes appear
            eye_rects = self.eye_cascade.detectMultiScale(face_roi,
                                                          scaleFactor=1.1,
                                                          minNeighbors=10,
                                                          minSize=(20, 20),
                                                          flags=cv2.CASCADE_SCALE_IMAGE)
            # loops over the bounding box regions of the eyes
            for (ex, ey, ew, eh) in eye_rects:
                rects.append((fx + ex, fy + ey, fx + ex + ew, fy + ey + eh))

        return rects
        