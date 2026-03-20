from abc import ABC, abstractmethod

from cv2.typing import MatLike


class MorphologicalTransformation(ABC):
    @abstractmethod
    def apply(
        self: "MorphologicalTransformation",
        image: MatLike,
        kernel: MatLike,
        iterations: int,
    ) -> MatLike:
        pass
