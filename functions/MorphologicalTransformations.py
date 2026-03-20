from dataclasses import dataclass
import cv2 as cv
import numpy as np


class MorphologicalTransformations:
    @staticmethod
    def dilation(image, kernel_size=(5, 5), iterations=1):
        kernel = np.ones(kernel_size, np.uint8)
        return cv.dilate(image, kernel, iterations=iterations)

    @staticmethod
    def erosion(image, kernel_size=(5, 5), iterations=1):
        kernel = np.ones(kernel_size, np.uint8)
        return cv.erode(image, kernel, iterations=iterations)

    @staticmethod
    def opening(image, kernel_size=(5, 5), iterations=1):
        kernel = np.ones(kernel_size, np.uint8)
        return cv.morphologyEx(image, cv.MORPH_OPEN, kernel, iterations=iterations)

    @staticmethod
    def closing(image, kernel_size=(5, 5), iterations=1):
        kernel = np.ones(kernel_size, np.uint8)
        return cv.morphologyEx(image, cv.MORPH_CLOSE, kernel, iterations=iterations)