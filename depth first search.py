def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    if start not in visited:
        print(start, end=' ')
        visited.add(start)
        for neighbor in graph[start] - visited: 
            dfs(graph, neighbor, visited)

# Example Usage:            
graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F', 'G'},
    'D': {'B'},
    'E': {'B'},
    'F': {'C'},
    'G': {'C'}
}

print("\nDFS:")
dfs(graph, 'A')
