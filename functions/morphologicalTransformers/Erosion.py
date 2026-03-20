import cv2 as cv
import numpy as np
from .MorphologicalTransformation import MorphologicalTransformation


class Erosion (MorphologicalTransformation):

    def apply(image, kernel_size=(5, 5), iterations=1):
        kernel = np.ones(kernel_size, np.uint8)
        return cv.erode(image, kernel, iterations=iterations)