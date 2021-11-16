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

    def test_get_start_space_2x3(self):
        maze = Maze(data_2x3)
        start = maze.get_start_space()
        self.assertEqual(start, [1, 2])

    def test_is_inbounds_right(self):
        maze = Maze(data_2x3)
        cell = maze.is_inbounds([1, 1])
        self.assertTrue(cell)

    def test_is_inbounds_wrong(self):
        maze = Maze(data_2x3)
        cell = maze.is_inbounds([3, 3])
        self.assertFalse(cell)

    def test_get_cell_wall(self):
        maze = Maze(data_2x3)
        cell = maze.get_cell([1, 1])
        self.assertEqual(cell, False)

    def test_get_cell_space(self):
        maze = Maze(data_2x3)
        cell = maze.get_cell([1, 2])
        self.assertEqual(cell, True)

    def test_get_cell_out_of_bounds(self):
        maze = Maze(data_2x3)
        cell = maze.get_cell([3, 4])
        self.assertEqual(cell, None)

    def test_get_adjacent_spaces_from_beginning(self):
        maze = Maze(data_2x3)
        start = [1, 2]
        neighbors = maze.get_adjacent_spaces(start)
        self.assertEqual(neighbors, [[2, 2]])

    def test_get_adjacent_spaces_from_middle(self):
        maze = Maze(data_6x4)
        start = [3, 3]
        neighbors = maze.get_adjacent_spaces(start)
        self.assertIn([4, 3], neighbors)
        self.assertIn([3, 2], neighbors)
