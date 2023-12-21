import heapq
def dijkstra(graph, start):
    # Create a priority queue to store vertices and their distances
    priority_queue = [(0, start)]
    # Create a dictionary to store the shortest distance to each vertex
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    while priority_queue:
        # Get the vertex with the smallest distance
        current_distance, current_vertex = heapq.heappop(priority_queue)
        # Check if the current distance is already larger than the stored distance
        if current_distance > distances[current_vertex]:
            continue
        # Iterate over the neighbors of the current vertex
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            # If a shorter path is found, update the distance
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    return distances
# Define a graph as an adjacency list
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 8},
    'D': {'B': 5, 'C': 8}
}
# Find the shortest paths from 'A' to all other vertices
start_vertex = 'A'
shortest_distances = dijkstra(graph, start_vertex)

print(f"Shortest distances from {start_vertex}: {shortest_distances}")
total_distance = sum(int(distance) for distance in shortest_distances.values())
print("Total distance:", total_distance)
