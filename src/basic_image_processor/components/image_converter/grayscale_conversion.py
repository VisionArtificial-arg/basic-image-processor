import cv2
from cv2.typing import MatLike
from cv2 import UMat


class GrayScaleConverter:
    def apply(self: "GrayScaleConverter", image: MatLike | UMat) -> MatLike | UMat:
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
