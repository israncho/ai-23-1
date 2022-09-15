class Puzzle:
    """Class to model the 8 puzzle."""

    def __init__(self, board):
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
        self.__previous_state = None
        self.__previous_move = None
        for i in range(3):
            for j in range(3):
                if board[i][j] == ():
                    self.__position = [i, j]
        if self.__position == None:
            raise Exception("Invalid board.")

    def __str__(self):
        """Function to return the string representation of the puzzle."""
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

    def __eq__(self, puzzle):
        """__eq__ implementation for Puzzle."""
        if type(puzzle) != type(self):
            return False
        if puzzle.__position != self.__position:
            return False
        for i in range(3):
            for j in range(3):
                if puzzle.__board[i][j] != self.__board[i][j]:
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

    def copy(self):
        """Returns a copy of this Puzzle on its current state."""
        return Puzzle(self.__board.copy())

    def set_previous(self, move, previous_puzzle):
        """Sets a previous state of this Puzzle."""
        if move not in ["up", "down", "left", "right"]:
            raise Exception("Wrong or invalid move: '" + str(move))
        if type(previous_puzzle) != type(self):
            raise Exception("Second argument is no a puzzle.")
        prev_copy = previous_puzzle.copy()
        print(prev_copy)
        prev_copy.move(move)
        print(prev_copy)
        if prev_copy != self: 
            raise Exception("Not a previous state of the Puzzle.")
        self.__previous_state = previous_puzzle
        self.__previous_move = move
    
    def get_previous_move(self):
        """Returns the previous move of this Puzzle."""
        return self.__previous_move

    def get_previous_state(self):
        """Returns the previous state of this Puzzle."""
        return self.__previous_state

    def valid_moves(self):
        """Returns all the valid moves of the current board."""
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
        """Makes a move on the current board."""
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


l = [[1, (), 2], [6, 3, 4], [7, 5, 8]]
l1 = [[(), 1, 2], [6, 3, 4], [7, 5, 8]]
puzzle = Puzzle(l)
puzzle1 = Puzzle(l1) 
puzzle.set_previous("right", puzzle1)
print(puzzle.get_previous_state() == puzzle1)
