import heapq

def prim(graph):
    mst = []  # Initialize the minimum spanning tree as an empty list
    visited = set()  # Initialize a set to keep track of visited vertices
    
    # Choose an arbitrary starting vertex
    start_vertex = next(iter(graph))
    visited.add(start_vertex)
    
    # Priority queue to store edges (weight, vertex1, vertex2)
    pq = [(weight, start_vertex, neighbor) for neighbor, weight in graph[start_vertex]]
    heapq.heapify(pq)
    
    while pq:
        weight, vertex1, vertex2 = heapq.heappop(pq)
        if vertex2 not in visited:
            visited.add(vertex2)
            mst.append((vertex1, vertex2, weight))
            for neighbor, weight in graph[vertex2]:
                if neighbor not in visited:
                    heapq.heappush(pq, (weight, vertex2, neighbor))
    
    return mst

# Example graph represented as an adjacency list
graph = {
    'A': [('B', 5), ('C', 3)],
    'B': [('A', 5), ('C', 2), ('D', 1)],
    'C': [('A', 3), ('B', 2), ('D', 3)],
    'D': [('B', 1), ('C', 3)]
}

# Find the minimum spanning tree using Prim's algorithm
minimum_spanning_tree = prim(graph)
print("Minimum Spanning Tree:", minimum_spanning_tree)
