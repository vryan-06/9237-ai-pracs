class State:
    def __init__(self, m, c, b):
        self.m = m  # number of missionaries on left side
        self.c = c  # number of cannibals on left side
        self.b = b  # 1 if boat is on left side, 0 if on right side

    def __repr__(self):
        return f"{self.m}M-{self.c}C-{self.b}B"

    def is_goal(self):
        return self.m == 0 and self.c == 0

    def is_valid(self):
        if self.m < 0 or self.c < 0 or self.m > 3 or self.c > 3 or (self.b != 0 and self.b != 1):
            return False
        if self.c > self.m and self.m != 0:
            return False
        if 3 - self.c > 3 - self.m and 3 - self.m != 0:
            return False
        return True

    def __eq__(self, other):
        return self.m == other.m and self.c == other.c and self.b == other.b

    def __hash__(self):
        return hash((self.m, self.c, self.b))

def successors(state):
    children = []
    if state.b == 1:
        # boat is on left side
        for i in range(3):
            for j in range(3):
                if i + j > 0 and i + j <= 2:
                    new_state = State(state.m - i, state.c - j, 0)
                    if new_state.is_valid():
                        children.append(new_state)
    else:
        # boat is on right side
        for i in range(3):
            for j in range(3):
                if i + j > 0 and i + j <= 2:
                    new_state = State(state.m + i, state.c + j, 1)
                    if new_state.is_valid():
                        children.append(new_state)
    return children

def dfs(start, goal):
    frontier = [[start]]
    visited = set()

    while frontier:
        path = frontier.pop()
        node = path[-1]

        if node.is_goal():
            return path

        for child in successors(node):
            if child not in visited:
                visited.add(child)
                new_path = path + [child]
                frontier.append(new_path)

    return None

start_state = State(3, 3, 1)
goal_state = State(0, 0, 0)
solution = dfs(start_state, goal_state)

if solution is None:
    print("No solution found!")
else:
    print("Solution found:")
    for i, state in enumerate(solution):
        if i == 0:
            print(f"Step {i+1}: Initial State is {state}")
        elif i == len(solution)-1:
            print(f"Step {i+1}: Reached Goal State {state}")
        elif state.b == 0:
            print(f"Step {i+1}: {state}")
        else:
            print(f"Step {i+1}: {state} ")