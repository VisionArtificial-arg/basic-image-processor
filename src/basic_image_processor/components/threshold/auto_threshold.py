import cv2
from cv2.typing import MatLike
from cv2 import UMat

from .base import ThresholdApplier


# Otsu's Thresholding after Gaussian Blur
class AutomaticThreshold(ThresholdApplier):
    def apply(self: ThresholdApplier, image: MatLike | UMat) -> MatLike | UMat:
        blurred = cv2.GaussianBlur(image, (5, 5), 0)
        _, result_image = cv2.threshold(
            blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
        )
        return result_image
