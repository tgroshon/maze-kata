import unittest
from ..lib.maze import Maze

data_2x3 = [
    [False, True, False],
    [False, True, False],
]

data_6x4 = [
    [False, True, False, False],
    [False, True, False, False],
    [False, True, True, False],
    [False, False, True, False],
    [False, False, True, False],
    [False, False, True, False],
]


class TestMaze(unittest.TestCase):
    def test_shape_with_2x3(self):
        maze = Maze(data_2x3)

        self.assertEqual(maze.shape.rows, 2)
        self.assertEqual(maze.shape.columns, 3)

    def test_shape_with_6x4(self):
        maze = Maze(data_6x4)

        self.assertEqual(maze.shape.rows, 6)
        self.assertEqual(maze.shape.columns, 4)

    def test_get_row_3(self):
        maze = Maze(data_6x4)
        self.assertIs(maze.get_row(3), data_6x4[2])

    def test_get_row_0_fails(self):
        maze = Maze(data_6x4)
        with self.assertRaises(Exception):
            maze.get_row(0)
