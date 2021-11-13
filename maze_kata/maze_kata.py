from wand.image import Image


def solve(img_path):
    img = Image(filename=img_path)
    print(f"Dimensions of '{img_path}':", img.width, "x", img.height)
