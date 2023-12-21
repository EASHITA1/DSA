def floyd_warshall(graph):
    nV = len(graph)
    INF = float('inf')
    # Create and initialize the distance matrix
    distance = [[INF if i != j else 0 for j in range(nV)] for i in range(nV)]
    # Initialize distance matrix based on the graph
    for i in range(nV):
        for j in range(nV):
            if i != j and graph[i][j] != 0:
                distance[i][j] = graph[i][j]
    # Floyd-Warshall algorithm
    for k in range(nV):
        for i in range(nV):
            for j in range(nV):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

    return distance
# Example usage:
graph = [
    [0, 3, float('inf'), 5, float('inf')],
    [2, 0, float('inf'), 4, float('inf')],
    [float('inf'), 1, 0, float('inf'), float('inf')],
    [float('inf'), float('inf'), 2, 0, float('inf')],
    [float('inf'), float('inf'), float('inf'), 1, 0]
]
result = floyd_warshall(graph)
# Printing the result
for row in result:
    print(row)
