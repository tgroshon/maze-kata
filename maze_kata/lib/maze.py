from collections import namedtuple
from numpy import array_equal
from dataclasses import dataclass


class Maze:
    """Intermediate representation of a maze

    Rules:
     - 1-based rows and columns
     - Adjacent means top, down, left, right. No diagonals.
    """

    Shape = namedtuple("MazeShape", ("rows columns"))

    def __init__(self, parsed_data):
        self._parsed_data = parsed_data

    @property
    def data(self):
        return self._parsed_data

    @property
    def shape(self):
        if not hasattr(self, "_shape"):
            self._shape = Maze.Shape(len(self.data), len(self.data[0]))

        return self._shape

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

    def get_start_space(self):
        """Address of first open space on the first row

        NOTE: assumes that there is only one entrance
        """
        idx = self.data[0].index(True)
        if not idx:
            return None

        return (1, idx + 1)

    def get_end_space(self):
        """Address of first open space on the last row

        NOTE: assumes that there is only one exit
        """
        last_row = self.shape.rows
        idx = self.data[last_row - 1].index(True)
        if not idx:
            return None

        return (last_row, idx + 1)

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

        """
        [row, col] = address

        left = (row, col - 1)
        right = (row, col + 1)
        below = (row + 1, col)
        above = (row - 1, col)

        return [
            neighbor
            for neighbor in (left, right, above, below)
            if self.is_inbounds(neighbor) and self.get_cell(neighbor)
        ]
