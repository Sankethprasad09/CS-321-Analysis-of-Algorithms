def solve_tsp(G):
    # The number of vertices/nodes
    N = len(G)

    # The start node
    start_node = 0

    # Create a visited array to mark nodes that have been visited
    visited = [False] * N

    # Mark the start node as visited
    visited[start_node] = True

    # Initialize the solution path with the start node
    path = [start_node]

    # Continue until all nodes have been visited
    while len(path) < N:
        min_distance = float('inf')
        min_index = -1

        # For the current node, find the nearest unvisited neighbor
        for i in range(N):
            if not visited[i] and G[path[-1]][i] > 0 and G[path[-1]][i] < min_distance:
                min_distance = G[path[-1]][i]
                min_index = i

        # Mark the nearest neighbor as visited and add it to the path
        visited[min_index] = True
        path.append(min_index)

    # Append the start node at the end of the path to make a cycle
    path.append(start_node)

    return path


# Define the graph
G = [
[0, 2, 3, 20, 1],
[2, 0, 15, 2, 20],
[3, 15, 0, 20, 13],
[20, 2, 20, 0, 9],
[1, 20, 13, 9, 0],
]

# Call the function
path = solve_tsp(G)

print("Path: ", path)

