def travelling_salesman_problem(n, cost_matrix):
    # Initialization
    path = [0] * (n + 1) # to store the path taken
    visited = [False] * n # to keep track of visited nodes
    total_cost = 0
    current_node = 0
    
    # Start with node 1
    path[0] = 1
    visited[0] = True
    
    # Find the shortest path to the next unvisited node
    for i in range(1, n):
        minimum = float('inf')
        for j in range(n):
            if not visited[j] and cost_matrix[current_node][j] < minimum:
                minimum = cost_matrix[current_node][j]
                next_node = j
        visited[next_node] = True
        path[i] = next_node+1
        total_cost += minimum
        current_node = next_node
    
    # Return the visited cities and total cost
    path[n] = 1
    total_cost += cost_matrix[current_node][0]
    print("The shortest path found is: ", path)
    print("The total cost of the shortest path is: ", total_cost)


# Take input for the number of cities
n = int(input("Enter the number of cities: "))

# Take input for the cost matrix
cost_matrix = []
print("Enter the cost matrix:")
for i in range(n):
    row = list(map(int, input().split()))
    cost_matrix.append(row)

# Call the travelling_salesman_problem function
travelling_salesman_problem(n, cost_matrix)