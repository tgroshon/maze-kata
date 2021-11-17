import cv2 as cv
from .maze import Maze


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


def generate_solution_image(input_img, solution):
    """Generate an image of the maze solution"""
    for row, col in solution:
        rpx, cpx = _calc_centerpoint_of_cell(row, col)
        cv.circle(
            input_img, center=(cpx, rpx), radius=10, color=(0, 0, 255), thickness=-1
        )
    return input_img


CELL_HEIGHT = 63  # ± 1 px
CELL_HEIGHT_MID = CELL_HEIGHT // 2
CELL_WIDTH = 87  # ± 1 px
CELL_WIDTH_MID = CELL_WIDTH // 2


def parse_maze_data(cv_img):
    """Parse an image into an intermediate representation of booleans representing maze spaces"""
    (h, w, _) = cv_img.shape

    # floor division to get integers
    rows = h // CELL_HEIGHT
    columns = w // CELL_WIDTH

    return [
        [_identify_cell(cv_img, r + 1, c + 1) for c in range(columns)]
        for r in range(rows)
    ]


def _identify_cell(img, row_num, col_num):
    """Identify if a cell is a space with a boolean"""
    row, col = _calc_centerpoint_of_cell(row_num, col_num)
    [blue, green, red] = img[row, col]

    # NOTE: Only set cell to empty if it's true white
    return blue == 255 and green == 255 and red == 255


def _calc_centerpoint_of_cell(row_num, col_num):
    """Calculate the centerpoint of a cell by row and column"""
    row_offset = (row_num - 1) * CELL_HEIGHT
    row = CELL_HEIGHT_MID + row_offset

    col_offset = (col_num - 1) * CELL_WIDTH
    col = CELL_WIDTH_MID + col_offset
    return row, col
