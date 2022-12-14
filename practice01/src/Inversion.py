import State
import Node

def toNP(state:  State.state):
    copy = state.copy()
    board = copy.get_board()
    return board[0] + board[1] + board[2]

def getInvCount(arr):
    inv_count = 0
    empty_value = -1
    for i in range(0, 9):
        for j in range(i + 1, 9):
            if arr[j] != () and arr[i] != () and arr[i] > arr[j]:
                inv_count += 1
    return inv_count

# This function returns true if given 8 puzzle array is solvable.
def isSolvable(arr) :
 
    # Count inversions in given 8 puzzle
    inv_count = getInvCount(arr)
 
    # return true if inversion count is even.
    return (inv_count % 2 == 0)

#goal_state = State.state([[1, 2, 3], [4, 5, 6], [7, 8, ()]])
#notSolvable = State.state([[8, 1, 2], [(), 4, 3], [7, 6, 5]])
#aux1= toNP(notSolvable)
#aux1 = np.concatenate((boardDT[0],boardDT[1],boardDT[2]))
#print("Number of inversions: ",getInvCount(aux1))
#print("Is solvable? ", isSolvable(aux1))
#print(aux1)
#print(type(aux1))