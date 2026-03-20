import cv2
from cv2.typing import MatLike
from cv2 import UMat

from .base import ThresholdApplier


# Apply Adaptive Gaussian Thresholding
class AdaptiveGaussThreshold(ThresholdApplier):
    def apply(self: ThresholdApplier, image: MatLike | UMat) -> MatLike | UMat:
        return cv2.adaptiveThreshold(
            image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
        )
