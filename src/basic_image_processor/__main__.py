import cv2 as cv

from basic_image_processor.components.image_converter import (
    GrayScaleConverter,
)

image = "./images/messi.jpg"
cv.imwrite("./images/bw.jpg", GrayScaleConverter().apply(cv.imread(image)))
