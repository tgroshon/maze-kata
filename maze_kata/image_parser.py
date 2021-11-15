import cv2 as cv


def parse(img_path):
    img = cv.imread(img_path)
    return MKImage(img_path, img)


# Wrapper class for custom behavior
class MKImage:
    def __init__(self, name, cv_img):
        self._name = name
        self._raw_image = cv_img

    @property
    def name(self):
        return self._name

    @property
    def height(self):
        (h, _, _) = self._raw_image.shape
        return h

    @property
    def width(self):
        (_, w, _) = self._raw_image.shape
        return w
