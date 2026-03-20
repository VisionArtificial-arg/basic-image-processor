from abc import ABC, abstractmethod


class MorphologicalTransformation(ABC):
    @abstractmethod
    def apply(self, image, kernel_size=(5, 5), iterations=1):
        pass

