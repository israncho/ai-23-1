from time import sleep
import State
import Node
import sys
import json
import Inversion
from collections import defaultdict


def dfs(state: State.state):
    stack = list()
    initial_state = state
    goal_state = State.state([[1, 2, 3], [4, 5, 6], [7, 8, ()]])
    first_node = Node.node(initial_state)
    stack.append(first_node)
    visited = defaultdict(lambda: False)
    nodes_visited = 0
    print("\ninitial state:\n")
    print(initial_state)
    print("\ngoal state:\n")
    print(goal_state)
    print("\n----------------starting in---------------\n3")
    sleep(2)
    print("2")
    sleep(2)
    print("1\n\n")
    while stack != []:
        nodes_visited += 1
        current_node = stack.pop()
        current_state = current_node.get_state()
        visited[str(current_state)] = True
        print(current_node)
        if current_state == goal_state:
            break
        for move in current_state.valid_moves():
            new_state = current_state.copy()
            new_state.move(move)
            if not visited[str(new_state)]:
                new_node = Node.node(new_state)
                new_node.set_previous(move, current_node)
                stack.append(new_node)

    print("\nNodes visited: ", end="")
    print(nodes_visited)
    #print("\nPrinting backtrack solution...\n")
    #sleep(2)
    solution_moves = -1
    while current_node != None:
        solution_moves += 1
        #print(current_node)
        current_node = current_node.get_previous_node()
    print("Moves to solve: ", end="")
    print(solution_moves)


initial_state = None
board = None
try:
    board = json.loads(sys.argv[1])
    print("input: ", end="")
    print(board)
    for i in range(3):
        for j in range(3):
            if board[i][j] == "e":
                board[i][j] = ()
except Exception as e:
    print("Wrong state of the puzzle :(")
    print(e)

try:
    state = State.state(board)
    print(state)
    stateNP = Inversion.toNP(state)
    if Inversion.isSolvable(stateNP):
        print("Is solvable because the number of inversions is", Inversion.getInvCount(stateNP), "and this number is     even :D")
        dfs(state)
    else:
        print("It has no solution because the number of inversions is ", Inversion.getInvCount(stateNP), "and this number is odd, try another state :)")
except Exception as e:
    print(e)
