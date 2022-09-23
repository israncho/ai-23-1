import State

class Node:
    def __init__(self, puzzle: State.state):
        if type(puzzle) != State.state:
            raise Exception("Wrong argument. Not a state of the 8-puzzle.")
        self.__puzzle = puzzle
        self.__previous_state = None
        self.__previous_move = None

    def set_previous(self, move, previous_puzzle):
        """Sets a previous state of this state."""
        if move not in ["up", "down", "left", "right"]:
            raise Exception("Wrong or invalid move: '" + str(move))
        if type(previous_puzzle) != type(self):
            raise Exception("Second argument is no a puzzle.")
        prev_copy = previous_puzzle.copy()
        print(prev_copy)
        prev_copy.move(move)
        print(prev_copy)
        if prev_copy != self:
            raise Exception("Not a previous state of the state.")
        self.__previous_state = previous_puzzle
        self.__previous_move = move

    def get_previous_move(self):
        """Returns the previous move of this state."""
        return self.__previous_move

    def get_previous_state(self):
        """Returns the previous state of this state."""
        return self.__previous_state

l = [[1, (), 2], [6, 3, 4], [7, 5, 8]]
l1 = [[(), 1, 2], [6, 3, 4], [7, 5, 8]]
puzzle = State.state(l)
puzzle1 = State.state(l1)
print(puzzle)