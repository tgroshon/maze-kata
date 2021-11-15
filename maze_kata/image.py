import cv2 as cv


def digitize_maze_image(img_path):
    """Read the image at file path and turn into intermediate representation"""
    img = cv.imread(img_path)
    maze_data = parse_maze(img)
    return Maze(img, maze_data)


def output_solution_image(output_path, maze, solution):
    """Write the maze solution to an image at output path"""
    img = generate_solution_image(maze, solution)
    cv.imwrite(output_path, img)


def generate_solution_image(maze, solution):
    """Generate an image of the maze solution

    FIXME: Placeholder; make this work
    """
    return maze.raw_image


def parse_maze(cv_img):
    """Parse an image into an intermediate representation of booleans representing maze spaces

    FIXME: Placeholder; make this work
    """
    return [[False, False, True, False], [False, False, True, False]]


class Maze:
    """Intermediate representation of a maze"""

    def __init__(self, cv_img, parsed_data):
        self._raw_image = cv_img
        self._parsed_data = parsed_data

    @property
    def data(self):
        return self._parsed_data

    @property
    def raw_image(self):
        return self._raw_image

    # TODO: remove these bottom debugging properties

    @property
    def pixel_height(self):
        (h, _, _) = self._raw_image.shape
        return h

    @property
    def pixel_width(self):
        (_, w, _) = self._raw_image.shape
        return w
