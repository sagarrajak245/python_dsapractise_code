import heapq

def dijkstra(graph, source):
    # Initialize distances dictionary with infinity for all vertices except the source
    distances = {vertex: float('inf') for vertex in graph}
    distances[source] = 0
    
    # Priority queue to store (distance, vertex) pairs
    pq = [(0, source)]
    heapq.heapify(pq)
    
    while pq:
        # Pop the vertex with the smallest distance from the priority queue 
        current_distance, current_vertex = heapq.heappop(pq)
        
        # Check if the current distance is already greater than the stored distance
        if current_distance > distances[current_vertex]:
            continue
        
        # Relaxation: Update distances for neighbors of the current vertex
        for neighbor, weight in graph[current_vertex].items():  
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances

# Example graph represented as an adjacency list (dictionary)
graph = {
    'A': {'B': 5, 'C': 3},
    'B': {'A': 5, 'C': 2, 'D': 1},
    'C': {'A': 3, 'B': 2, 'D': 3},
    'D': {'B': 1, 'C': 3}
}

# Source vertex
source_vertex = 'A'

# Find shortest paths from the source vertex using Dijkstra's algorithm
shortest_paths = dijkstra(graph, source_vertex)
print("Shortest paths from", source_vertex + ":", shortest_paths)
