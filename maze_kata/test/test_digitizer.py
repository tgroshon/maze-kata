import unittest
import os
import cv2 as cv
from ..lib.digitizer import parse_maze_data

SINGLE_ROW_IMG = os.path.join("assets", "us1_single_row.png")
HALLWAY_IMG = os.path.join("assets", "us2_hallway.png")
ROOM_IMG = os.path.join("assets", "us3_room.png")
WINDING_IMG = os.path.join("assets", "us4_winding.png")
DEADENDS_IMG = os.path.join("assets", "us5_simple.png")


class TestParseMaze(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.hallway_img = cv.imread(HALLWAY_IMG)
        cls.deadends_img = cv.imread(DEADENDS_IMG)

    def test_hallway_asset_size(self):
        data = parse_maze_data(self.hallway_img)

        self.assertEqual(len(data), 4)
        self.assertEqual(len(data[0]), 4)

    def test_hallway_parse(self):
        data = parse_maze_data(self.hallway_img)

        self.assertEqual(
            data,
            [
                [False, False, True, False],
                [False, False, True, False],
                [False, False, True, False],
                [False, False, True, False],
            ],
        )

    def test_deadends_asset_size(self):
        data = parse_maze_data(self.deadends_img)

        self.assertEqual(len(data), 6)
        self.assertEqual(len(data[0]), 5)

    def test_deadends_parse(self):
        data = parse_maze_data(self.deadends_img)
        self.assertEqual(
            data,
            [
                [False, True, False, False, False],
                [False, True, True, True, False],
                [False, True, False, False, False],
                [False, True, True, True, False],
                [False, True, False, True, False],
                [False, False, False, True, False],
            ],
        )
