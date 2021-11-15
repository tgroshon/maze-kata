import cv2 as cv

def solve(img_path):
    img = cv.imread(img_path)
    (height, width, _) = img.shape
    print(f"Dimensions of '{img_path}':", width, "x", height)
