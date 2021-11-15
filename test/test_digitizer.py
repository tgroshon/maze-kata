import unittest
import cv2 as cv
from maze_kata.digitizer import parse_maze_data

SINGLE_ROW_IMG = "./assets/single_row_us1.png"
HALLWAY_IMG = "./assets/hallway_us2.png"
ROOM_IMG = "./assets/room_us3.png"
WINDING_IMG = "./assets/winding_path_us4.png"
DEADENDS_IMG = "./assets/simple_maze_us5.png"


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
