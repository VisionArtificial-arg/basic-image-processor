from dataclasses import dataclass
from typing import Any, Iterator

import cv2 as cv


@dataclass(frozen=True)
class Contours:
    contours: list
    hierarchy: Any

    def __iter__(self) -> Iterator[Any]:
        yield from self.contours

    @classmethod
    def get_contours(
        cls,
        image,
        mode: int = cv.RETR_EXTERNAL,
        method: int = cv.CHAIN_APPROX_SIMPLE,
    ) -> "Contours":
        contours, hierarchy = cv.findContours(image, mode, method)
        return cls(contours=contours, hierarchy=hierarchy)
