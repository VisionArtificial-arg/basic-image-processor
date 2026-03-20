import cv2


class GrayScale:
        def apply(self, image):
                return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


