import cv2 as cv
import numpy as np

def closing(image,kernel_size=(5,5),iterations=1):
    kernel = np.ones(kernel_size, np.uint8)
    return cv.morphologyEx(image, cv.MORPH_CLOSE, kernel, iterations=iterations)