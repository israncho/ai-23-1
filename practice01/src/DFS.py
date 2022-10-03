from time import sleep
import State
import Node
from collections import defaultdict

stack = list()
initial_state = State.state([[1, 2, 3],[4, 5, 6],[(), 7, 8]])
goal_state = State.state([[1, 2, 3],[4, 5, 6],[7, 8, ()]])
first_node = Node.node(initial_state)
stack.append(first_node)
visited = defaultdict(lambda: False)
nodes_visited = 0
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

print("\nNodes visited: ",end="")
print(nodes_visited)
print("\nPrinting backtrack solution...\n")
sleep(5)
solution_moves = -1
while current_node != None:
    solution_moves += 1
    print(current_node)
    current_node = current_node.get_previous_node()
print("Moves to solve: ", end="")
print(solution_moves)