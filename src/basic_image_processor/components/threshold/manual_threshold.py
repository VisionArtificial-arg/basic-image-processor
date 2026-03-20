import cv2
from cv2.typing import MatLike
from cv2 import UMat


class ManualThreshold:
    def apply(
        self, image: MatLike | UMat, value: float, max: float, type: int
    ) -> MatLike | UMat:
        _, th = cv2.threshold(image, value, max, type)
        return th
