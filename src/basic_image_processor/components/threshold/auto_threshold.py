import cv2


# Otsu's Thresholding after Gaussian Blur

class AutomaticThreshold:
    def apply(self, image):
        blurred = cv2.GaussianBlur(image, (5,5), 0)
        _, result_image = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        return result_image