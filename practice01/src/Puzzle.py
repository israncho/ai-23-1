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
        self.board = board
        self.position = None
        for i in range(3):
            for j in range(3):
                if board[i][j] == ():
                    self.position = [i, j]
        if self.position == None:
            raise Exception("Invalid board.")

    def __str__(self):
        """Function to return the string representation of the puzzle."""
        string = ""
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ():
                    string = string + "   "
                else:
                    string = string + str(self.board[i][j]) + "  "
            if i < 2:
                string = string + "\n"
        return string

    def __swap(self, row1, col1, row2, col2):
        """Private function to swap elements on the board."""
        to_verify = [row1, col1, row2, col2]
        for element in to_verify:
            if element > 2 or element < 0:
                raise Exception("Positions out of bounds.")
        temp_element = self.board[row1][col1]
        self.board[row1][col1] = self.board[row2][col2]
        self.board[row2][col2] = temp_element

    def valid_moves(self):
        """Returns all the valid moves of the current board."""
        moves = []
        row = self.position[0]
        col = self.position[1]
        if row > 0:
            moves.append('up') 
        if row < 2:
            moves.append('down')
        if col > 0:
            moves.append('left')
        if col < 2:
            moves.append('right')
        return moves

    def move(self, move, copy=False):
        """Makes a move on the current board."""
        valid_moves = self.valid_moves()
        if move not in valid_moves:
            raise Exception("Wrong or invalid move: \'" + str(move) + "\' for board:\n" + self.__str__() )
        curr_pos = self.position.copy()
        if move == 'up':
            self.position[0] = self.position[0] - 1
        if move == 'down':
            self.position[0] = self.position[0] + 1
        if move == 'left':
            self.position[1] = self.position[1] - 1
        if move == 'up':
            self.position[0] = self.position[1] + 1
        self.__swap(self.position[0], self.position[1], curr_pos[0], curr_pos[1])
        



puzzle = Puzzle([[1, (), 2], [6, 3, 4], [7, 5, 8]])
print(puzzle)
print(puzzle.valid_moves())
puzzle.move('down')
print(puzzle)
print(puzzle.valid_moves())
puzzle.move('down')
print(puzzle)
print(puzzle.valid_moves())
puzzle.move('down')
print(puzzle)
print(puzzle.valid_moves())