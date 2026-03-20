import cv2


# Apply Adaptive Gaussian Thresholding
class AdaptiveGaussThreshold:
    def apply(self, image):
        return cv2.adaptiveThreshold(
            image,
            255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY,
            11,
            2
        )