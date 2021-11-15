from collections import namedtuple


class Maze:
    """Intermediate representation of a maze

    Rules:
     - 1-based rows and columns
    """

    Shape = namedtuple("MazeShape", ("rows columns"))

    def __init__(self, cv_img, parsed_data):
        self._raw_image = cv_img
        self._parsed_data = parsed_data

    @property
    def data(self):
        return self._parsed_data

    @property
    def raw_image(self):
        return self._raw_image

    @property
    def shape(self):
        if not hasattr(self, "_shape"):
            self._shape = Maze.Shape(len(self.data), len(self.data[0]))

        return self._shape

    def get_row(self, row_num):
        if row_num <= 0:
            raise Exception(f"Rows are 1-based, got: {row_num}")

        return self.data[row_num - 1]
