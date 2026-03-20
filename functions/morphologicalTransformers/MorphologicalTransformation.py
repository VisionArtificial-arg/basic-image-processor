from abc import ABC, abstractmethod

class MorphologicalTransformation(ABC):

    @abstractmethod
    def apply(image, kernel_size=(5, 5), iterations=1):
        pass