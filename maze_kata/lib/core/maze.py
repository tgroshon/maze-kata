from collections import namedtuple


class MalformedMazeError(Exception):
    pass


class Maze:
    """Intermediate representation of a maze

    Rules:
     - 1-based rows and columns
     - Adjacent means top, down, left, right. No diagonals.
    """

    Shape = namedtuple("Shape", ("rows columns"))

    def __init__(self, parsed_data):
        self._parsed_data = parsed_data

    def cell_iter(self):
        for ri in range(self.shape.rows):
            for ci in range(self.shape.columns):
                cell = (ri + 1, ci + 1)
                if self.get_cell(cell):
                    yield cell

    @property
    def data(self):
        return self._parsed_data

    @property
    def shape(self):
        if not hasattr(self, "_shape"):
            self._shape = Maze.Shape(len(self.data), len(self.data[0]))

        return self._shape

    def is_branch(self, address):
        return len(self.get_adjacent_spaces(address)) > 2

    def is_end(self, address):
        """Does address match the end space?"""
        return address == self.get_end_space()

    def is_start(self, address):
        """Does address match the start space?"""
        return address == self.get_start_space()

    def is_deadend(self, address):
        """Is the given address a cell a deadend?"""
        if self.is_end(address) or self.is_start(address):
            return False

        return len(self.get_adjacent_spaces(address)) <= 1

    def is_inbounds(self, address):
        """Is a given address in the bounds of the maze?"""
        row, col = address
        return (
            row > 0 and col > 0 and row <= self.shape.rows and col <= self.shape.columns
        )

    def fill_space(self, address):
        """MUTATES the maze data by setting an address to be a wall; idempotent"""
        if not self.is_inbounds(address):
            raise Exception(
                f"Attempting to fill a space that is not in bounds: {address}"
            )

        r, c = address
        self.data[r - 1][c - 1] = False

    def get_start_space(self):
        """Address of first open space on the first row

        NOTE: assumes that there is only one entrance
        """
        try:
            idx = self.data[0].index(True)
            return (1, idx + 1)
        except ValueError:
            raise MalformedMazeError("Missing Start. No space found on the first row.")

    def get_end_space(self):
        """Address of first open space on the last row

        NOTE: assumes that there is only one exit
        """
        last_row = self.shape.rows
        try:
            idx = self.data[last_row - 1].index(True)
            return (last_row, idx + 1)
        except ValueError:
            raise MalformedMazeError("Missing End. No space found on the last row.")

    def get_cell(self, address):
        """Get contents of cell at address"""
        if not self.is_inbounds(address):
            return None

        row, col = address
        return self.data[row - 1][col - 1]

    def get_adjacent_spaces(self, address):
        """List all space addresses adjacent to given address

        NOTE: the ordering returned by this method has significant bearing on
        the efficiency of the solving algorithm. Consider moving this code to
        the solver?

        NOTE: Practical runs indicate that, due to the mazes the program
        encounters, the priority should always be to:
          1. Move downward.
          2. When reaching a bottom wall, move side-to-side.
          3. Almost never move up. Most solutions NEVER move up.

        """
        [row, col] = address

        left = (row, col - 1)
        right = (row, col + 1)
        below = (row + 1, col)
        above = (row - 1, col)

        return [
            neighbor
            for neighbor in (above, left, right, below)
            if self.is_inbounds(neighbor) and self.get_cell(neighbor)
        ]
