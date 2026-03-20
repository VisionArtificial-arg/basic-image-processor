import cv2
from .base import MorphologicalTransformation
from cv2.typing import MatLike


class Erosion(MorphologicalTransformation):
    def apply(
        self: "MorphologicalTransformation",
        image: MatLike,
        kernel: MatLike,
        iterations: int,
    ) -> MatLike:
        return cv2.erode(image, kernel, iterations=iterations)
