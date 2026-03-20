import cv2 as cv
from .base import MorphologicalTransformation
from cv2.typing import MatLike


class Dilation(MorphologicalTransformation):
    def apply(
        self: "MorphologicalTransformation",
        image: MatLike,
        kernel: MatLike,
        iterations: int,
    ) -> MatLike:
        return cv.dilate(image, kernel, iterations=iterations)
