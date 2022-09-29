import unittest
import State
import random


class StateUnitTest(unittest.TestCase):
    """Class for the unit testing of the State class."""

    def test_valid_moves(self):
        """Test for the function State.state.valid_moves()"""
        print("state.valid_moves() ", end=" -> ")
        state = State.state([[(), 0, 0], [0, 0, 0], [0, 0, 0]])
        self.assertTrue(set(state.valid_moves()) == set(["down", "right"]))
        state = State.state([[0, (), 0], [0, 0, 0], [0, 0, 0]])
        self.assertTrue(set(state.valid_moves()) == set(["down", "right", "left"]))
        state = State.state([[0, 0, ()], [0, 0, 0], [0, 0, 0]])
        self.assertTrue(set(state.valid_moves()) == set(["down", "left"]))
        state = State.state([[0, 0, 0], [(), 0, 0], [0, 0, 0]])
        self.assertTrue(set(state.valid_moves()) == set(["up", "down", "right"]))
        state = State.state([[0, 0, 0], [0, (), 0], [0, 0, 0]])
        self.assertTrue(
            set(state.valid_moves()) == set(["up", "down", "right", "left"])
        )
        state = State.state([[0, 0, 0], [0, 0, ()], [0, 0, 0]])
        self.assertTrue(set(state.valid_moves()) == set(["up", "down", "left"]))
        state = State.state([[0, 0, 0], [0, 0, 0], [(), 0, 0]])
        self.assertTrue(set(state.valid_moves()) == set(["up", "right"]))
        state = State.state([[0, 0, 0], [0, 0, 0], [0, (), 0]])
        self.assertTrue(set(state.valid_moves()) == set(["up", "right", "left"]))
        state = State.state([[0, 0, 0], [0, 0, 0], [0, 0, ()]])
        self.assertTrue(set(state.valid_moves()) == set(["up", "left"]))
        print("PASSED")

    def random_boards(diff_board: list):
        """Generates a list of boards different to the board passed as argument."""
        if type(diff_board) != list or len(diff_board) > 3:
            raise Exception("Invalid board :(.")

        for i in range(3):
            if type(diff_board[i]) != list or len(diff_board[i]) > 3:
                raise Exception("Invalid board.")

        for i in range(3):
            for j in range(3):
                if type(diff_board[i][j]) != tuple and type(diff_board[i][j]) != int:
                    raise Exception("Invalid board.")

        elements = [1, 2, 3, 4, 5, 6, 7, 8, ()]
        boards = list()
        for e in range(1000):
            elements = [1, 2, 3, 4, 5, 6, 7, 8, ()]
            current = list()
            for i in range(3):
                row = list()
                for j in range(3):
                    row.append(elements.pop(random.randrange(len(elements))))
                current.append(row)
            # print(current)
            if diff_board != current:
                boards.append(current)
        return boards

    def test_eq(self):
        """Test for the __eq__ function of State."""
        print("state.__eq__()", end=" -> ")
        state = State.state([[(), 1, 2], [3, 4, 5], [6, 7, 8]])
        for board in StateUnitTest.random_boards([[(), 1, 2], [3, 4, 5], [6, 7, 8]]):
            other_state = State.state(board)
            self.assertFalse(state == other_state)
        other_state = State.state([[(), 1, 2], [3, 4, 5], [6, 7, 8]])
        self.assertTrue(other_state == state)

        state = State.state([[5, 1, 2], [3, 4, ()], [6, 7, 8]])
        for board in StateUnitTest.random_boards([[5, 1, 2], [3, 4, ()], [6, 7, 8]]):
            other_state = State.state(board)
            self.assertFalse(state == other_state)
        other_state = State.state([[5, 1, 2], [3, 4, ()], [6, 7, 8]])
        self.assertTrue(other_state == state)
        print("PASSED")

    def test_copy(self):
        """Test for the function State.state.copy()"""
        print("state.copy() ", end=" -> ")
        state = State.state([[(), 1, 2], [3, 4, 5], [6, 7, 8]])
        copy = state.copy()
        self.assertTrue(id(copy) != id(state))
        self.assertTrue(copy == state)
        copy.move("right")
        self.assertTrue(id(copy) != id(state))
        self.assertFalse(copy == state)
        print("PASSED")


if __name__ == "__main__":
    print("Tests for State class\n")
    unittest.main()
