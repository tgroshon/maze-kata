import os
import unittest
import cv2 as cv
import tempfile
from ..lib.digitizer import (
    parse_maze_image,
    output_solution_image,
)

US1_SINGLE_ROW_IMG = os.path.join("assets", "us1_single_row.png")
US2_HALLWAY_IMG = os.path.join("assets", "us2_hallway.png")
US3_ROOM_IMG = os.path.join("assets", "us3_room.png")
US3_ROOM_SOLUTION_IMG = os.path.join("assets", "solutions", "us3_room_solution.png")
US4_WINDING_IMG = os.path.join("assets", "us4_winding.png")
US5_DEADENDS_IMG = os.path.join("assets", "us5_simple.png")


class TestDigitizeIntegration(unittest.TestCase):
    def test_digitize_maze_us1(self):
        maze = parse_maze_image(US1_SINGLE_ROW_IMG)
        self.assertEqual(maze.data, [[False, True, False, False, False, False, False]])

    def test_digitize_maze_us2(self):
        maze = parse_maze_image(US2_HALLWAY_IMG)
        self.assertEqual(
            maze.data,
            [
                [False, False, True, False],
                [False, False, True, False],
                [False, False, True, False],
                [False, False, True, False],
            ],
        )

    def test_digitize_maze_us3(self):
        maze = parse_maze_image(US3_ROOM_IMG)
        self.assertEqual(
            maze.data,
            [
                [False, True, False, False, False],
                [False, True, True, True, False],
                [False, True, True, True, False],
                [False, False, False, True, False],
            ],
        )

    def test_digitize_maze_us4(self):
        maze = parse_maze_image(US4_WINDING_IMG)
        self.assertEqual(
            maze.data,
            [
                [False, True, False, False, False],
                [False, True, True, True, False],
                [False, False, False, True, False],
                [False, True, True, True, False],
                [False, True, False, False, False],
                [False, True, True, True, False],
                [False, False, False, True, False],
            ],
        )

    def test_digitize_maze_us5(self):
        maze = parse_maze_image(US5_DEADENDS_IMG)
        self.assertEqual(
            maze.data,
            [
                [False, True, False, False, False],
                [False, True, True, True, False],
                [False, True, False, False, False],
                [False, True, True, True, False],
                [False, True, False, True, False],
                [False, False, False, True, False],
            ],
        )


class TestOutputSolutionIntegration(unittest.TestCase):
    def assertSameImage(self, img1, img2):
        if img1.shape[:2] != img2.shape[:2]:
            raise AssertionError("Images are difference shapes")

        difference = cv.subtract(img1, img2)
        b, g, r = cv.split(difference)

        print(cv.countNonZero(b), cv.countNonZero(g), cv.countNonZero(r))
        if not (
            cv.countNonZero(b) == 0
            and cv.countNonZero(g) == 0
            and cv.countNonZero(r) == 0
        ):
            raise AssertionError("Images are difference colors")

    @unittest.skip("Assertion doesn't correctly compare images")
    def test_output_solution_us3(self):
        # US3_ROOM_SOLUTION_IMG
        with tempfile.NamedTemporaryFile(suffix="-test-solution.png") as fp:
            print("\n", fp.name)

            output_solution_image(
                US3_ROOM_IMG, fp.name, [(1, 2), (2, 2), (3, 2), (3, 3), (3, 4), (4, 4)]
            )

            self.assertSameImage(cv.imread(US3_ROOM_SOLUTION_IMG), cv.imread(fp.name))
