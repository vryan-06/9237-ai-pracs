from queue import PriorityQueue
print("--- Missionaries Cannibals Problem Using Greedy Best-First Search ----")
print("\n")
m=int(input("Enter the number of missionaries:"))
c= int(input("Enter the number of cannibals:"))
b= int(input("Enter the side of the river where the boat is present(0 for left,1 for right):"))
print("\n")
print("--- Solution ---\n")
# define the initial state
initial_state = (m, c, b)

# define the goal state
goal_state = (0, 0, 0)

# define the set of valid actions
actions = [(1, 0), (0, 1), (2, 0), (0, 2), (1, 1)]

# define the heuristic function (using the number of missionaries and cannibals on the left bank)
def heuristic(state):
    return state[0] + state[1]

# define the search function
def search():
    # initialize the priority queue with the initial state and its heuristic value
    frontier = PriorityQueue()
    frontier.put((heuristic(initial_state), initial_state, []))
    # initialize the explored set
    explored = set()
    # loop until the goal state is found or the frontier is empty
    while not frontier.empty():
        # get the state with the lowest heuristic value
        _, current_state, path = frontier.get()
        # check if the current state is the goal state
        if current_state == goal_state:
            return path
        # add the current state to the explored set
        explored.add(current_state)
        # generate the successor states and their paths
        for action in actions:
            # check if the action is valid
            if current_state[2] == 1 and (current_state[0] - action[0] < current_state[1] - action[1] or
                                         current_state[0] - action[0] < 0 or
                                         current_state[1] - action[1] < 0):
                continue
            elif current_state[2] == 0 and ((current_state[0] + action[0] < current_state[1] + action[1] and
                                              current_state[0] + action[0] != 0) or
                                             current_state[0] + action[0] > 3 or
                                             current_state[1] + action[1] > 3):
                continue
            # generate the successor state and its path
            if current_state[2] == 1:
                successor_state = (current_state[0] - action[0], current_state[1] - action[1], 0)
            else:
                successor_state = (current_state[0] + action[0], current_state[1] + action[1], 1)
            successor_path = path + [(current_state, action, successor_state)]
            # check if the successor state has already been explored
            if successor_state in explored:
                continue
            # add the successor state and its path to the priority queue
            frontier.put((heuristic(successor_state), successor_state, successor_path))
    # if the goal state is not found, return None
    return None

# run the search function and print the result
result = search()
if result is not None:
    for i, step in enumerate(result):
        print("Step", i+1, ":")
        print("  ", step[0], "->", step[1], "->", step[2])
else:
    print("No solution found.")
