from dataclasses import dataclass
from typing import Any, Iterator

import cv2 as cv


@dataclass(frozen=True)
class Contours:
    contours: list
    hierarchy: Any

    def __iter__(self) -> Iterator[Any]:
        yield from self.contours

    def __init__(self, image, mode: int = cv.RETR_EXTERNAL, method: int = cv.CHAIN_APPROX_SIMPLE,) -> None :
        contours, hierarchy = cv.findContours(image, mode, method)
        object.__setattr__(self, "contours", contours)
        object.__setattr__(self, "hierarchy", hierarchy)
