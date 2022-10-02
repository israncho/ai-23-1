import copy


class state:
    """Class to model the state of the 8 puzzle."""

    def __init__(self, board: list):
        """Constructor of the puzzle with parameters."""
        if type(board) != list or len(board) > 3:
            raise Exception("Invalid board :(.")

        for i in range(3):
            if type(board[i]) != list or len(board[i]) > 3:
                raise Exception("Invalid board.")

        for i in range(3):
            for j in range(3):
                if type(board[i][j]) != tuple and type(board[i][j]) != int:
                    raise Exception("Invalid board.")

        self.__board = board
        self.__position = None

        for i in range(3):
            for j in range(3):
                if board[i][j] == ():
                    self.__position = [i, j]

        if self.__position == None:
            raise Exception("Invalid board.")

    def __str__(self):
        """Function to return the string representation of the state of the puzzle."""
        string = ""
        for i in range(3):
            for j in range(3):
                if self.__board[i][j] == ():
                    string = string + "   "
                else:
                    string = string + str(self.__board[i][j]) + "  "

            if i < 2:
                string = string + "\n"

        return string

    def __eq__(self, state):
        """__eq__ implementation for state."""
        if type(state) != type(self):
            return False

        if state.__position != self.__position:
            return False

        for i in range(3):
            for j in range(3):
                if state.__board[i][j] != self.__board[i][j]:
                    return False

        return True

    def __swap(self, row1: int, col1: int, row2: int, col2: int):
        """Private function to swap elements on the board."""
        to_verify = [row1, col1, row2, col2]
        for element in to_verify:
            if element > 2 or element < 0:
                raise Exception("Positions out of bounds.")

        temp_element = self.__board[row1][col1]
        self.__board[row1][col1] = self.__board[row2][col2]
        self.__board[row2][col2] = temp_element

    def get_board(self):
        """Returns a copy of the board."""
        return copy.deepcopy(self.__board)

    def get_position(self):
        """Returns the position in a tuple."""
        return (self.__position[0], self.__position[1])

    def copy(self):
        """Returns a copy of this state."""
        return state(copy.deepcopy(self.__board))

    def valid_moves(self):
        """Returns all the valid moves of the current state."""
        # The board:
        # [0,0] [0,1] [0,2]
        # [1,0] [1,1] [1,2]
        # [2,0] [2,1] [2,2]
        moves = []
        row = self.__position[0]
        col = self.__position[1]
        if row > 0:
            moves.append("up")
        if row < 2:
            moves.append("down")
        if col > 0:
            moves.append("left")
        if col < 2:
            moves.append("right")
        return moves

    def move(self, move):
        """Makes a move on the current state."""
        valid_moves = self.valid_moves()
        if move not in valid_moves:
            raise Exception(
                "Wrong or invalid move: '"
                + str(move)
                + "' for board:\n"
                + self.__str__()
            )
        curr_pos = self.__position.copy()
        if move == "up":
            self.__position[0] = self.__position[0] - 1
        if move == "down":
            self.__position[0] = self.__position[0] + 1
        if move == "left":
            self.__position[1] = self.__position[1] - 1
        if move == "right":
            self.__position[1] = self.__position[1] + 1
        self.__swap(self.__position[0], self.__position[1], curr_pos[0], curr_pos[1])

edoI = [[1, (), 2], [6, 3, 4], [7, 5, 8]]
puzzle = state(edoI)
print(puzzle)
print(puzzle.get_position())
print(puzzle.valid_moves())
puzzle.move("right")
print(puzzle)
