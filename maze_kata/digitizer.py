import cv2 as cv
from maze import Maze


def digitize_maze_image(img_path):
    """Read the image at file path and turn into intermediate representation"""
    img = cv.imread(img_path)
    maze_data = parse_maze_data(img)
    return Maze(maze_data)


def output_solution_image(input_path, output_path, maze, solution):
    """Write the maze solution to an image at output path"""
    input_img = cv.imread(input_path)
    output_img = generate_solution_image(input_img, solution)
    cv.imwrite(output_path, output_img)


def generate_solution_image(maze, solution):
    """Generate an image of the maze solution

    FIXME: Placeholder; make this work
    """
    return maze.raw_image


def parse_maze_data(cv_img):
    """Parse an image into an intermediate representation of booleans representing maze spaces

    FIXME: Placeholder; make this work
    """
    return [[False, False, True, False], [False, False, True, False]]
