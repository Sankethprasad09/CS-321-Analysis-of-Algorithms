import heapq

def Prims(G):
    # Number of vertices in the graph
    num_vertices = len(G)
    
    # Array to store the minimum edge weight
    min_edge = [float('inf')] * num_vertices

    # Array to store the parent of a node in the MST
    parent = [-1] * num_vertices

    # Array to store whether a node is part of the MST
    in_mst = [False] * num_vertices

    # The MST starts from node 0
    min_edge[0] = 0

    # Priority queue as a list of tuples
    pq = [(0, 0)]  # (weight, node)

    while pq:
        # Get node with smallest weight
        _, u = heapq.heappop(pq)

        in_mst[u] = True

        for v in range(num_vertices):
            weight = G[u][v]

            # Proceed if v is not in mst and weight of (u,v) is smaller than current edge weight from v
            if not in_mst[v] and weight > 0 and weight < min_edge[v]:
                min_edge[v] = weight
                parent[v] = u
                heapq.heappush(pq, (weight, v))

    mst = []
    for i in range(1, num_vertices):
        mst.append((parent[i], i, G[i][parent[i]]))

    return mst


input_graph = [
    [0, 8, 5, 0, 0, 0, 0],
    [8, 0, 10, 2, 18, 0, 0],
    [5, 10, 0, 3, 0, 16, 0],
    [0, 2, 3, 0, 12, 30, 14],
    [0, 18, 0, 12, 0, 0, 4],
    [0, 0, 16, 30, 0, 0, 26],
    [0, 0, 0, 14, 4, 26, 0]
]

output_graph = Prims(input_graph)
print(output_graph)

