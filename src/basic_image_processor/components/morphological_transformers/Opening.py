import cv2
from .base import MorphologicalTransformation
from cv2.typing import MatLike


class Opening(MorphologicalTransformation):
    def apply(
        self: "MorphologicalTransformation",
        image: MatLike,
        kernel: MatLike,
        iterations: int,
    ) -> MatLike:
        return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel, iterations=iterations)
