import unittest
from ..lib.core import Maze, MalformedMazeError

data_2x3 = [
    [False, True, False],
    [False, True, False],
]

data_6x4 = [
    [False, True, False, False],
    [False, True, True, False],
    [False, True, False, False],
    [False, True, True, False],
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

    def test_get_start_space_2x3(self):
        maze = Maze(data_2x3)

        start = maze.get_start_space()

        self.assertEqual(start, (1, 2))

    def test_get_start_space_raises_for_no_start(self):
        maze = Maze(
            [
                [False, False, False],
                [False, True, False],
                [False, True, False],
            ]
        )

        with self.assertRaises(MalformedMazeError):
            maze.get_start_space()

    def test_is_inbounds_right(self):
        maze = Maze(data_2x3)

        cell = maze.is_inbounds((1, 1))

        self.assertTrue(cell)

    def test_is_inbounds_wrong(self):
        maze = Maze(data_2x3)

        cell = maze.is_inbounds((3, 3))

        self.assertFalse(cell)

    def test_get_cell_wall(self):
        maze = Maze(data_2x3)

        cell = maze.get_cell((1, 1))

        self.assertEqual(cell, False)

    def test_get_cell_space(self):
        maze = Maze(data_2x3)

        cell = maze.get_cell((1, 2))

        self.assertEqual(cell, True)

    def test_get_cell_out_of_bounds(self):
        maze = Maze(data_2x3)

        cell = maze.get_cell((3, 4))

        self.assertEqual(cell, None)

    def test_get_adjacent_spaces_from_beginning(self):
        maze = Maze(data_2x3)
        start = (1, 2)

        neighbors = maze.get_adjacent_spaces(start)

        self.assertEqual(neighbors, [(2, 2)])

    def test_get_adjacent_spaces_from_middle(self):
        maze = Maze(data_6x4)
        start = (4, 3)

        neighbors = maze.get_adjacent_spaces(start)

        self.assertEqual(len(neighbors), 2)
        self.assertIn((5, 3), neighbors)
        self.assertIn((4, 2), neighbors)

    def test_get_end_space(self):
        maze = Maze(data_6x4)

        end = maze.get_end_space()

        self.assertEqual(end, (6, 3))

    def test_get_end_space_raises_for_no_start(self):
        maze = Maze(
            [
                [False, True, False],
                [False, True, False],
                [False, False, False],
            ]
        )

        with self.assertRaises(MalformedMazeError):
            maze.get_end_space()

    def test_is_start(self):
        maze = Maze(data_6x4)

        start = (1, 2)

        self.assertTrue(maze.is_start(start))

    def test_is_end(self):
        maze = Maze(data_6x4)

        end = (6, 3)

        self.assertTrue(maze.is_end(end))

    def test_is_deadend(self):
        maze = Maze(data_6x4)

        deadend_address = (2, 3)

        self.assertTrue(maze.is_deadend(deadend_address))

    def test_is_not_deadend_on_start_and_end(self):
        maze = Maze(data_6x4)

        start = (1, 2)
        end = (6, 3)

        self.assertFalse(maze.is_deadend(start))
        self.assertFalse(maze.is_deadend(end))

    def test_cell_iter_2x3(self):
        maze = Maze(data_2x3)
        spaces = list(maze.cell_iter())
        self.assertEqual(spaces, [(1, 2), (2, 2)])

    def test_cell_iter_6x4(self):
        maze = Maze(data_6x4)
        spaces = list(maze.cell_iter())
        self.assertEqual(
            spaces, [(1, 2), (2, 2), (2, 3), (3, 2), (4, 2), (4, 3), (5, 3), (6, 3)]
        )

    def test_fill_space(self):
        maze = Maze(
            [
                [False, True, False],
                [False, True, False],
            ]
        )

        maze.fill_space((1, 2))

        self.assertEqual(
            maze.data,
            [
                [False, False, False],
                [False, True, False],
            ],
        )

    def test_fill_space_out_bounds(self):
        maze = Maze(
            [
                [False, True, False],
                [False, True, False],
            ]
        )

        with self.assertRaises(Exception):
            maze.fill_space((1, 4))

    def test_is_branch_false_on_path(self):
        maze = Maze(
            [
                [False, True, False, False],
                [False, True, False, False],
                [False, True, False, False],
            ]
        )

        self.assertFalse(maze.is_branch((2, 2)), "Expected not to be a branch")

    def test_is_branch_true_on_branch(self):
        maze = Maze(
            [
                [False, True, False, False],
                [False, True, True, False],
                [False, True, False, False],
            ]
        )

        self.assertTrue(maze.is_branch((2, 2)), "Expected to be a branch")
