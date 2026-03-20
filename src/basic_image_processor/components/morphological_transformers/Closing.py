import cv2
from cv2.typing import MatLike
from .base import MorphologicalTransformation


class Closing(MorphologicalTransformation):
    def apply(
        self: "MorphologicalTransformation",
        image: MatLike,
        kernel: MatLike,
        iterations: int,
    ) -> MatLike:
        return cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel, iterations=iterations)
