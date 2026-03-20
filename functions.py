import cv2 as cv
import numpy as np

def erotion(image,kernel_size=(5,5),iterations=1):
    kernel = np.ones(kernel_size, np.uint8)
    return cv.erode(image, kernel, iterations=iterations)

def dilation(image,kernel_size=(5,5),iterations=1):
    kernel = np.ones(kernel_size, np.uint8)
    return cv.dilate(image, kernel, iterations=iterations)

def opening(image,kernel_size=(5,5),iterations=1):
    kernel = np.ones(kernel_size, np.uint8)
    return cv.morphologyEx(image, cv.MORPH_OPEN, kernel, iterations=iterations)

def closing(image,kernel_size=(5,5),iterations=1):
    kernel = np.ones(kernel_size, np.uint8)
    return cv.morphologyEx(image, cv.MORPH_CLOSE, kernel, iterations=iterations)

def contours(image,mode=cv.RETR_EXTERNAL,method=cv.CHAIN_APPROX_SIMPLE):
    img, contours, hierarchy = cv.findContours(image, mode, method)
    result = (img, contours, hierarchy)
    return result