from unicodedata import name
import unittest
import State


class StateUnitTest(unittest.TestCase):
    """Class for the unit testing of the State class."""

    def test_valid_moves(self):
        """Test for the function State.state.valid_moves()"""
        state = State.state([[(), 0, 0], [0, 0, 0], [0, 0, 0]])
        self.assertTrue(set(state.valid_moves()) == set(["down", "right"]))
        state = State.state([[0, (), 0], [0, 0, 0], [0, 0, 0]])
        self.assertTrue(set(state.valid_moves()) == set(["down", "right", "left"]))
        state = State.state([[0, 0, ()], [0, 0, 0], [0, 0, 0]])
        self.assertTrue(set(state.valid_moves()) == set(["down", "left"]))
        state = State.state([[0, 0, 0], [(), 0, 0], [0, 0, 0]])
        self.assertTrue(set(state.valid_moves()) == set(["up", "down", "right"]))
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


if __name__ == "__main__":
    unittest.main()
