from collections import defaultdict

def topological_sort_util(graph, vertex, visited, stack):
    visited[vertex] = True
    for neighbor in graph[vertex]:
        if not visited[neighbor]:
            topological_sort_util(graph, neighbor, visited, stack)
    stack.append(vertex)

def topological_sort(graph, vertices):
    visited = {vertex: False for vertex in vertices}
    stack = []
    for vertex in vertices:
        if not visited[vertex]:
            topological_sort_util(graph, vertex, visited, stack)
    return stack

def shortest_paths_dag(graph, source, destination):
    # Step 1: Topological Sorting
    vertices = list(graph.keys())
    top_order = topological_sort(graph, vertices)

    # Step 2: Initialization
    dist = {vertex: float('inf') for vertex in vertices}
    dist[source] = 0

    # Step 3: Dynamic Programming
    for u in top_order:
        for v, weight in graph[u].items():
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight

    # Step 4: Result
    return dist

# Example usage:
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'C': 2, 'D': 5},
    'C': {'D': 8},
    'D': {}
}

start_vertex = 'A'
destination_vertex = 'D'
result = shortest_paths_dag(graph, start_vertex, destination_vertex)
print(f"Shortest distances from {start_vertex} to {destination_vertex}: {result}")
