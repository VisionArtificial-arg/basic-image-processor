import cv2


class GrayScaleConverter:
    def apply(self, image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
