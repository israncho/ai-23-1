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
    
    def get_depth(self):
        return self.depth
    
    def set_depth(self, x):
        self.depth = x

    def __str__(self):
        return self.__state.__str__() + "\nprevious move : <"  + str(self.__previous_move)+ "> and with depth: "+ str(self.depth)

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
        newNodo.set_depth(nodo.get_depth() + 1)
        yield newNodo

def depth_limited_search(nodoI:node, limit):
    #l = [[1, (), 2], [6, 3, 4], [7, 5, 8]]
    #boardI= State.state(l)
    #initialN = node(boardI)
    initialN = nodoI
    finalS =State.state([[(), 1, 2], [3, 4, 5], [6, 7, 8]])
    front=[initialN]
    result = "path dont found"
    #print(type(finalS))
    print(finalS)
    while len(front) != 0:
        newNodo = front.pop()
        print(newNodo.get_state())
        print(newNodo.get_state().equ(finalS))
        if ((newNodo.get_state().equ(finalS))!=False):
            return newNodo
        if (newNodo.depth >= limit):
            result = "limit exceeded"
        else:
            for x in expand(newNodo):
                #print(x)
                #print(x.get_state().equ(finalS))
                front.append(x)
    return result

def writeR(nodo):
    if nodo.get_previous_node() == None:
        print(nodo.get_state())
        return
    father = nodo.get_previous_node()
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

li = [[1, (), 2], [3, 4, 5], [6, 7, 8]]
boardF = State.state(li)
nodeF = node(boardF)
print("\n--> Begin in node: ", nodeF)
result=depth_limited_search(nodeF, 10)
if (result == "path dont found" or result == "limit exceeded"):
        print(result)
else:
    writeR(result)
print("FIN <<")

    