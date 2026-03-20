import cv2


class ManualThreshold:
    def apply(self, frame, slider_max, binary, trackbar_value):
        _, th = cv2.threshold(frame, trackbar_value, slider_max, binary)
        return th
