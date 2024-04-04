def bellman_ford(graph, source):
    # Step 1: Initialize distances to all vertices as infinity
    distances = {vertex: float('inf') for vertex in graph}
    distances[source] = 0

    # Step 2: Relax edges repeatedly |V| - 1 times
    for _ in range(len(graph) - 1):
        for vertex in graph:
            for neighbor, weight in graph[vertex].items():
                if distances[vertex] + weight < distances[neighbor]:
                    distances[neighbor] = distances[vertex] + weight

    # Step 3: Check for negative cycles
    for vertex in graph:
        for neighbor, weight in graph[vertex].items():
            if distances[vertex] + weight < distances[neighbor]:
                raise ValueError("Graph contains a negative cycle")

    return distances

# Example usage:
graph = {
    'A': {'B': -1, 'C': 4},
    'B': {'C': 3, 'D': 2, 'E': 2},
    'C': {},
    'D': {'B': 1, 'C': 5},
    'E': {'D': -3}
}
source_vertex = 'A'
shortest_distances = bellman_ford(graph, source_vertex)
print(shortest_distances)

