from abc import ABC, abstractmethod

from cv2 import UMat
from cv2.typing import MatLike


class ThresholdApplier(ABC):
    @abstractmethod
    def apply(self: "ThresholdApplier", image: MatLike | UMat) -> MatLike | UMat:
        pass
