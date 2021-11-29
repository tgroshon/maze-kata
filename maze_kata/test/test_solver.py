import unittest
from ..lib.core import solve, DefaultStrategy, ImprovedStrategy, Maze


class TestSolve(unittest.TestCase):
    def test_returns_none_for_empty_maze(self):
        """Raise a NoSolutionFound exception if the Maze given is empty"""
        empty_maze = Maze(None)

        solution = solve(empty_maze)
        self.assertIsNone(solution, "Expected no solution for empty maze")

    def test_solve_accepts_alternate_strategy(self):
        one_step_data = [[False, False, True, False]]
        one_step_maze = Maze(one_step_data)

        class AltStrategy:
            def solve(self, maze):
                return ["Fake Solution"]

        solution = solve(one_step_maze, AltStrategy())

        self.assertEqual(solution, ["Fake Solution"])

    def test_finds_solution_for_one_step_maze(self):
        one_step_data = [[False, False, True, False]]
        one_step_maze = Maze(one_step_data)

        solution = solve(one_step_maze)
        self.assertIsNotNone(solution, "Must find a solution for a one-step maze")
        self.assertEqual(
            [(1, 3)],
            solution,
        )

    def test_finds_solution_for_hallway_maze(self):
        hallway_data = [
            [False, False, True, False],
            [False, False, True, False],
            [False, False, True, False],
        ]
        hallway_maze = Maze(hallway_data)

        solution = solve(hallway_maze)

        self.assertIsNotNone(solution, "Must find a solution for a hallway maze")
        self.assertEqual(solution, [(1, 3), (2, 3), (3, 3)])

    def test_finds_solution_for_following_winding_path(self):
        winding_path_data = [
            [False, True, False, False, False],
            [False, True, True, True, False],
            [False, False, False, True, False],
            [False, True, True, True, False],
            [False, True, False, False, False],
            [False, True, True, True, False],
            [False, False, False, True, False],
        ]
        winding_maze = Maze(winding_path_data)

        solution = solve(winding_maze)
        self.assertIsNotNone(solution, "Must find a solution for a winding path maze")
        self.assertEqual(
            solution,
            [
                (1, 2),
                (2, 2),
                (2, 3),
                (2, 4),
                (3, 4),
                (4, 4),
                (4, 3),
                (4, 2),
                (5, 2),
                (6, 2),
                (6, 3),
                (6, 4),
                (7, 4),
            ],
        )


class TestDefaultSolver(unittest.TestCase):
    def test_fill_deadends(self):
        strategy = DefaultStrategy()
        maze = Maze(
            [
                [False, True, False, False, False],
                [False, True, True, True, False],
                [False, True, False, False, False],
                [False, True, True, True, False],
                [False, True, False, True, False],
                [False, False, False, True, False],
            ]
        )

        strategy.fill_deadends(maze)

        self.assertEqual(
            maze.data,
            [
                [False, True, False, False, False],
                [False, True, False, False, False],
                [False, True, False, False, False],
                [False, True, True, True, False],
                [False, False, False, True, False],
                [False, False, False, True, False],
            ],
        )

    def test_fill_deadends_recursively(self):
        strategy = DefaultStrategy()
        maze = Maze(
            [
                [False, True, False, False, False, False],
                [False, True, False, True, True, False],
                [False, True, False, False, True, False],
                [False, True, True, True, True, True],
                [False, True, False, False, True, False],
                [False, True, True, True, False, False],
                [False, True, False, True, False, False],
                [False, False, False, True, False, False],
            ]
        )

        strategy.fill_deadends(maze)

        self.assertEqual(
            maze.data,
            [
                [False, True, False, False, False, False],
                [False, True, False, False, False, False],
                [False, True, False, False, False, False],
                [False, True, False, False, False, False],
                [False, True, False, False, False, False],
                [False, True, True, True, False, False],
                [False, False, False, True, False, False],
                [False, False, False, True, False, False],
            ],
        )

    def test_imperfect_maze(self):
        """solver finds one solution in a maze with a loop"""
        strategy = DefaultStrategy()
        maze = Maze(
            [
                [False, True, False, False, False],
                [False, True, True, True, False],
                [False, True, False, True, False],
                [False, True, False, True, False],
                [False, True, True, True, False],
                [False, False, False, True, False],
            ]
        )

        solution = strategy.solve(maze)

        self.assertEqual(
            solution, [(1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (5, 3), (5, 4), (6, 4)]
        )

    def test_returns_none_for_unsolveable_maze(self):
        strategy = DefaultStrategy()
        maze = Maze(
            [
                [False, True, False, False, False],
                [False, True, True, True, False],
                [False, True, False, True, False],
                [False, True, False, True, False],
                [False, True, False, False, False],
                [False, False, False, True, False],  # "exit" is cut-off from "start"
            ]
        )

        solution = strategy.solve(maze)
        self.assertIsNone(solution)


class TestImprovedStrategy(unittest.TestCase):
    @unittest.skip("Known to break")
    def test_removes_backtracking(self):
        """solver finds one solution in a maze with a loop"""
        strategy = ImprovedStrategy()
        maze = Maze(
            [
                [False, True, False, False, False],
                [False, True, True, True, False],
                [False, True, False, True, False],
                [False, True, False, True, False],
                [False, True, False, True, False],
                [False, False, False, True, False],
            ]
        )

        solution = strategy.solve(maze)

        self.assertEqual(
            solution, [(1, 2), (2, 2), (2, 3), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4)]
        )

    def test_imperfect_maze(self):
        """solver finds one solution in a maze with a loop"""
        strategy = ImprovedStrategy()
        maze = Maze(
            [
                [False, True, False, False, False],
                [False, True, True, True, False],
                [False, True, False, True, False],
                [False, True, False, True, False],
                [False, True, True, True, False],
                [False, False, False, True, False],
            ]
        )

        solution = strategy.solve(maze)

        self.assertEqual(
            solution, [(1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (5, 3), (5, 4), (6, 4)]
        )

    def test_returns_none_for_unsolveable_maze(self):
        strategy = ImprovedStrategy()
        maze = Maze(
            [
                [False, True, False, False, False],
                [False, True, True, True, False],
                [False, True, False, True, False],
                [False, True, False, True, False],
                [False, True, False, False, False],
                [False, False, False, True, False],  # "exit" is cut-off from "start"
            ]
        )

        solution = strategy.solve(maze)
        self.assertIsNone(solution)
