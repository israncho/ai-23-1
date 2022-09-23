import State


class node:
    """Class to model a wrapper node for  a state of the 8-puzzle."""

    def __init__(self, puzzle: State.state):
        if type(puzzle) != State.state:
            raise Exception("Wrong argument. Not a state of the 8-puzzle.")
        self.__state = puzzle
        self.__previous_node = None
        # Move to get to the current state
        self.__previous_move = None

    def __str__(self):
        return self.__state.__str__() + "\nprevious move: " + str(self.__previous_move)

    def get_state(self):
        return self.__state

    def set_previous(self, move, previous_node):
        """Sets a previous state of this state."""
        if move not in ["up", "down", "left", "right"]:
            raise Exception("Wrong or invalid move: '" + str(move))
        if type(previous_node) != type(self):
            raise Exception("Second argument is no a node.")
        prev_copy = previous_node.__state.copy()
        # print(prev_copy)
        prev_copy.move(move)
        # print(prev_copy)
        if prev_copy != self.__state:
            raise Exception("Not a previous state of this state.")
        self.__previous_node = previous_node
        self.__previous_move = move

    def get_previous_move(self):
        """Returns the previous move of this state."""
        return self.__previous_move

    def get_previous_node(self):
        """Returns the previous state of this state."""
        return self.__previous_node


l = [[1, (), 2], [6, 3, 4], [7, 5, 8]]
l1 = [[(), 1, 2], [6, 3, 4], [7, 5, 8]]
puzzle = State.state(l)
puzzle1 = State.state(l1)
node1 = node(puzzle)
node2 = node(puzzle1)
node1.set_previous("right", node2)
print("\n-------------\n")
print(node2)
print(node1)
print("\n-------------\n")
print(node2)
print(node1.get_previous_node())
