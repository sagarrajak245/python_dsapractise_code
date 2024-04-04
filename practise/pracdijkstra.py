
# import heapq

# def dijkstra(graph,source):
    
    
#     distances={vertex:float('inf') for vertex in graph}
#     distances[source]=0
    
    
#     #priority queue  initialize
    
#     pq= [(0,source)]
    
#     heapq.heapify(pq)
    
    
#     while pq:
        
#         cur_distance,cur_vertex= heapq.heappop(pq)
#         if cur_distance>distances[cur_vertex]:
#             continue
        
        
        
#         #now iterate thorugh graph 
        
#         for neighbour,weight in graph[cur_vertex].items():
#              # now calculate curr distance
       
#             distance=cur_distance+weight
#             if distance<distances[neighbour]:
#                 distances[neighbour]= distance
    
    
#                 heapq.heappush(pq,(distance,neighbour))
    
    
#     return distances 
                
        
    



# graph ={
    
#     # 'a':{'b':5,'c':3},
#     # 'b':{'a':5,'c':10,'d':2},
#     # 'c':{'b':10,'d':3,'a':3},
#     # 'd':{'b':2,'c':3},
    
#     'A': {'B': 5, 'C': 3},
#     'B': {'A': 5, 'C': 2, 'D': 1},
#     'C': {'A': 3, 'B': 2, 'D': 3},
#     'D': {'B': 1, 'C': 3}
    
# }

# source='A'
# shortest_distance= dijkstra(graph,source)
# print('shortest distance from source vertex:'+ source +'is',shortest_distance )

import heapq


def dijkstra(graph,source):
    distances={vertex: float ('inf') for vertex in graph}
    distances[source]=0
    
   # initialize priority queue
    pq =[(0,source)]
    
    heapq.heapify(pq)
    
    
    
    while pq:
        
        cur_distance,cur_vertex=heapq.heappop(pq)
        
        if cur_distance>distances[cur_vertex]:
            continue
        
        for neighbour,weight in graph[cur_vertex].items():
            
            distance= cur_distance+weight
            
            if distance< distances[neighbour]:
                distances[neighbour]=distance
                heapq.heappush(pq,(weight,neighbour))
    return distances   
        
        
    
    
    

graph={
    
    'a':{'b':5,'c':8,'d':3},
    'b':{'a':5,'c':8,'d':7},
    'c':{'b':8,'a':8,'d':3},
    'd':{'b':7,'c':3,'a':3},
    
}

source='a'
shortest_distance=dijkstra(graph,source)

print('shortest path from vertex is'+ source+'is',shortest_distance)
