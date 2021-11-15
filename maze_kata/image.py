import cv2 as cv


def digitize_maze_image(img_path):
    img = cv.imread(img_path)
    mk_image = Maze(img)
    # mk_image.parse_maze()
    return mk_image


def output_solution_image(img_path, maze, solution):
    img = generate_solution_image(maze, solution)
    cv.imwrite(img_path, img)


def generate_solution_image(maze, solution):
    pass


# Wrapper class for custom behavior
class Maze:
    def __init__(self, cv_img):
        self._raw_image = cv_img

    def parse_maze():
        pass

    @property
    def raw_image(self):
        return self._raw_image

    @property
    def name(self):
        return self._name

    @property
    def pixel_height(self):
        (h, _, _) = self._raw_image.shape
        return h

    @property
    def pixel_width(self):
        (_, w, _) = self._raw_image.shape
        return w
