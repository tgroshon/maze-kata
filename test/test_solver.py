import unittest
import maze_kata.solver as solver
from maze_kata.maze import Maze


class TestNoSolutionException(unittest.TestCase):
    def test_no_solution_found_is_exception(self):
        """NoSolutionFound is a subclass of Exception"""
        self.assertIsInstance(solver.NoSolutionFound(), Exception)


class TestSolve(unittest.TestCase):
    def test_returns_none_for_empty_maze(self):
        """Raise a NoSolutionFound exception if the Maze given is empty"""
        empty_maze = Maze(None, None)

        solution = solver.solve(empty_maze)
        self.assertIsNone(solution, "Expected no solution for empty maze")

    def test_finds_solution_for_one_step_maze(self):
        one_step_data = [[False, False, True, False]]
        one_step_maze = Maze(None, one_step_data)

        solution = solver.solve(one_step_maze)
        self.assertIsNotNone(solution, "Must find a solution for a one-step maze")
        self.assertEqual(
            [[1, 3]],
            solution,
        )

    @unittest.skip("Known to be missing")
    def test_finds_solution_for_hallway_maze(self):
        hallway_data = [[False, False, True, False], [False, False, True, False]]
        hallway_maze = Maze(None, hallway_data)

        solution = solver.solve(hallway_maze)
        self.assertIsNotNone(solution, "Must find a solution for a hallway maze")
