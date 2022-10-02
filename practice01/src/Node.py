from ast import While
import State
import string

class node:
    """Class to model a wrapper node for  a state of the 8-puzzle."""

    def __init__(self, puzzle: State.state):
        """Constructor of the node."""
        if type(puzzle) != State.state:
            raise Exception("Wrong argument. Not a state of the 8-puzzle.")
        self.__state = puzzle
        self.__previous_node = None #parent
        # Move to get to the current state
        self.__previous_move = None
        self.depth = 0
    
    def set_depth(self, x):
        self.depth = x

    def __str__(self):
        return self.__state.__str__() + "\nprevious move : "  + str(self.__previous_move)+ "and with depth "+ str(self.depth)

    def get_state(self):
        """Function to get the state of the node"""
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

def expand(nodo:node):
    "Expande el nodo"
    stateI = nodo.get_state()
    validM = stateI.valid_moves()
    for x in validM:
        oldState = stateI.copy()
        oldState.move(x)
        newNodo = node(oldState)
        newNodo.set_previous(x,nodo)
        newNodo.set_depth(nodex.depth + 1)
        yield newNodo

def depth_limited_search(nodoI:node, limit):
    #l = [[1, (), 2], [6, 3, 4], [7, 5, 8]]
    #boardI= State.state(l)
    #initialN = node(boardI)
    initialN = nodoI
    front=[initialN]
    result = "path dont found"
    while len(front) != 0:
        newNodo = front.pop()
        if (newNodo.get_state() == State.state([[(), 1, 2], [3, 4, 5], [6, 7, 8]])):
            return newNodo
        if (newNodo.depth >= limit):
            result = "limit exceeded"
        else:
            for x in expand(newNodo):
                print(x)
                print(x.get_state().get_board()==[[(), 1, 2], [3, 4, 5], [6, 7, 8]])
                #front.append(x)
    return result

def writeR(nodo):
    if get_previous_node(nodo) == None:
        print(nodo.get_state)
        return
    father = nodo.get_previous_node
    writeR(father)
    print(father)
    return string

l2 = [[1, 3, 2], [6, (), 4], [7, 5, 8]]
l = [[1, (), 2], [6, 3, 4], [7, 5, 8]]
l1 = [[(), 1, 2], [6, 3, 4], [7, 5, 8]]
puzzle = State.state(l)
puzzle1 = State.state(l1)
puzzle2 = State.state(l2)
# nodo recibe un state
node1 = node(puzzle)
node2 = node(puzzle1)
node3 = node(puzzle2)
node3.set_previous("down", node1) # node3=l2, node
node1.set_previous("right", node2) # node1=l, node2=l1

lx = [[(), 1, 2], [6, 3, 4], [7, 5, 8]]
boardX = State.state(lx)
nodex = node(boardX)
print("Nodo base:\n",nodex,"\n")
for i in expand(nodex):
    print(i)

lf = [[(), 1, 2], [3, 4, 5], [6, 7, 9]]
boardF = State.state(lf)
nodeF = node(boardF)
if (nodeF.get_state() == State.state([[(), 1, 2], [3, 4, 5], [6, 7, 8]])):
    print("1")
else: 
    print("F")

li = [[1, (), 2], [3, 4, 5], [6, 7, 9]]
boardF = State.state(li)
nodeF = node(boardF)
print("\n--> Begin in node: ", nodeF)
result=depth_limited_search(nodeF, 10)
if (result == "path dont found" or resultado == "limit exceeded"):
        print(result)
else:
    writeR(result)
print("FIN <<")

    