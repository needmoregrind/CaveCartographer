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
        self.assertEqual(adv_1.visited, [[1],[1]])
        self.assertEqual(adv_1.cave.layout,TestMove1.TEST_CAVE_1_LAYOUT)

class TestMove2(unittest.TestCase) :
    # LAYOUT 2 #

    TEST_CAVE_2_LAYOUT = [
        ["R"], ["R"], ["R"], ["R"], ["R"],
        ["R"], ["S"], ["_"], ["R"], ["R"],
        ["R"], ["_"], ["_"], ["_"], ["R"],
        ["R"], ["_"], ["E"], ["_"], ["R"],
        ["R"], ["R"], ["R"], ["R"], ["R"],
        ]

    def setup_cave_2():
        cave_2 = Cave("")
        cave_2.layout = TestMove2.TEST_CAVE_2_LAYOUT
        adv = Adventure(cave_2)
        return cave_2, adv

    def test_setup_2(self):
        cave_2, adv_2 = TestMove2.setup_cave_2()
        self.assertEqual(adv_2.current_spot,[0,0])
        self.assertEqual(adv_2.visited,[[0],[1]])
        self.assertEqual(adv_2.cave.layout,TestMove2.TEST_CAVE_2_LAYOUT)

     ## Test Can Move 2
    def test_can_move_down_2(self):
        cave_2, adv_2 = TestMove2.setup_cave_2()
        valid_move = adv_2.can_move("down")
        self.assertTrue(valid_move)

    def test_can_move_up_2(self):
        direction = "up"
        cave_2, adv_2 = TestMove2.setup_cave_2()
        valid_move = adv_2.can_move(direction)
        self.assertFalse(valid_move, "Cannot move "+
                         direction+" in cave 2")

    def test_can_move_left_2(self):
        direction = "left"
        cave_2, adv_2 = TestMove2.setup_cave_2()
        valid_move = adv_2.can_move(direction)
        self.assertFalse(valid_move, 
                         "Cannot move "+direction+ " in cave 2")

    def test_can_move_right_2(self):   
        direction = "right"
        cave_2, adv_2 = TestMove2.setup_cave_2()
        valid_move = adv_2.can_move(direction)
        # if was anything other than bool, would also want to
        # check type
        self.assertTrue(valid_move)

    def test_can_move_to_exit(self):
        direction = 'right'
        cave_2, adv_2 = TestMove2.setup_cave_2()
        adv_2.current_spot = [2, 0]
        valid_move = adv_2.can_move(direction)
        self.assertTrue(valid_move)

    def test_cannot_move_out_of_bounds(self):
        direction1 = 'up'
        direction2 = 'left'
        cave_2, adv_2 = TestMove2.setup_cave_2()
        adv_2.current_spot = [0,0]
        valid_move1 = adv_2.can_move(direction1)
        valid_move2 = adv_2.can_move(direction2)
        self.assertFalse(valid_move1)
        self.assertFalse(valid_move2)
    
    def test_at_the_exit(self):
        cave_2, adv_2 = TestMove2.setup_cave_2()
        adv_2.current_spot = [2, 1]
        self.assertEqual(adv_2.current_spot, 'Adventurer has reached the exit!')

    ## Test Move
    # only test moving down, all other moves invalid
    def test_move_down_2(self):
        cave_2, adv_2 = TestMove2.setup_cave_2()
        adv_2.move("down")
        self.assertEqual(adv_2.current_spot, [0,0])
        self.assertEqual(adv_2.visited, [[1],[0]],)
        self.assertEqual(adv_2.cave.layout,TestMove2.TEST_CAVE_2_LAYOUT)

    def test_move_up_2(self):
        cave_2, adv_2 = TestMove2.setup_cave_2()
        adv_2.move('up')
        self.assertEqual(adv_2.current_spot, [2, 0])
        self.assertEqual(adv_2.visited, [[1], [0]])
        self.assertEqual(adv_2.cave.layout, TestMove2.TEST_CAVE_2_LAYOUT)

    def test_move_left_2(self):
        cave_2, adv_2 = TestMove2.setup_cave_2()
        adv_2.move('left')
        self.assertEqual(adv_2.current_spot, [1, 1])
        self.assertEqual(adv_2.visited, [[1], [0]])
        self.assertEqual(adv_2.cave.layout, TestMove2.TEST_CAVE_2_LAYOUT)

    def test_move_right_2(self):
        cave_2, adv_2 = TestMove2.setup_cave_2()
        adv_2.move('right')
        self.assertEqual(adv_2.current_spot, [0, 0])
        self.assertEqual(adv_2.visited, [[0], [1]])
        self.assertEqual(adv_2.cave.layout, TestMove2.TEST_CAVE_2_LAYOUT)
     
    def test_move_out_of_bounds(self):
        cave_2, adv_2 = TestMove2.setup_cave_2()
        adv_2.current_spot, [0, 0]
        adv_2.move('left')
        self.assertEqual(adv_2.current_spot, [[0], [0]])

    def test_move_out_of_bounds(self):
        cave_2, adv_2 = TestMove2.setup_cave_2()
        adv_2.current_spot, [0, 0]
        adv_2.move('up')
        self.assertEqual(adv_2.current_spot, [[0], [0]])

    def test_move_into_end(self):
        cave_2, adv_2 = TestMove2.setup_cave_2()
        adv_2.current_spot, [1, 1]
        adv_2.move('down')
        self.assertEqual(adv_2.current_spot, [[2], [1]])

if __name__ =='__main__':
    unittest.main()