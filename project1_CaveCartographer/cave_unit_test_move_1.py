import unittest
from io import StringIO
import sys

from project1_solution import Cave, Adventure

class TestMove1(unittest.TestCase) :
    # LAYOUT 1 #

    TEST_CAVE_1_LAYOUT = [
        ["S"],
        ["E"]
        ]

    def setup_cave_1():
        cave_1 = Cave("")
        cave_1.layout = TestMove1.TEST_CAVE_1_LAYOUT
        adv = Adventure(cave_1)
        return cave_1, adv

    def test_setup_1(self):
        cave_1, adv_1 = TestMove1.setup_cave_1()
        self.assertEqual(adv_1.current_spot,[0,0])
        self.assertEqual(adv_1.visited,[[1],[1]])
        self.assertEqual(adv_1.cave.layout,TestMove1.TEST_CAVE_1_LAYOUT)

    ## Test Can Move
    def test_can_move_down_1(self):
        cave_1, adv_1 = TestMove1.setup_cave_1()
        valid_move = adv_1.can_move("down")
        self.assertTrue(valid_move)

    def test_can_move_up_1(self):
        direction = "up"
        cave_1, adv_1 = TestMove1.setup_cave_1()
        valid_move = adv_1.can_move(direction)
        self.assertFalse(valid_move, "Cannot move "+
                         direction+" in cave 1")

    def test_can_move_left_1(self):
        direction = "left"
        cave_1, adv_1 = TestMove1.setup_cave_1()
        valid_move = adv_1.can_move(direction)
        self.assertFalse(valid_move, 
                         "Cannot move "+direction+ " in cave 1")

    def test_can_move_right_1(self):
            direction = "right"
            cave_1, adv_1 = TestMove1.setup_cave_1()
            valid_move = adv_1.can_move(direction)
            # if was anything other than bool, would also want to
            # check type
            self.assertFalse(valid_move, 
                            "Cannot move "+direction+ " in cave 1")

    ## Test Move
    # only test moving down, all other moves invalid
    def test_move_down_1(self):
        cave_1, adv_1 = TestMove1.setup_cave_1()
        adv_1.move("down")
        self.assertEqual(adv_1.current_spot, [1,0])
        self.assertEqual(adv_1.visited, [[1],[1]],)
        self.assertEqual(adv_1.cave.layout,TestMove1.TEST_CAVE_1_LAYOUT)


unittest.main()