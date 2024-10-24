from collections import deque

def bfs_8puzzle(initial_state):
    goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    queue = deque([(initial_state, [])])  
    visited = set()

    while queue:
        state, path = queue.popleft()
        if state == goal_state: # u found the goal state now show the path
            return path
        
        #else add the state to visited and add its neighbors to the queue
        visited.add(tuple(map(tuple, state))) # path add kara 
        for neighbor in get_neighbors(state): # get the neighbors of the current state
            if tuple(map(tuple, neighbor)) not in visited: # if the neighbor is not visited then add it to the queue
                queue.append((neighbor, path + [neighbor]))

def get_neighbors(state):
    neighbors = []
    # Find the position of the empty tile (0)
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                x, y = i, j
                break
        if state[i][j] == 0:
            break
    
    # Define possible moves (up, down, left, right)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for dx, dy in moves: # for each move check if the new position is within the grid
        nx, ny = x + dx, y + dy
        # Check if the new position is within the grid
        if 0 <= nx < 3 and 0 <= ny < 3:
            # Create a new state by swapping the empty tile
            new_state = [row[:] for row in state]  # copy the state
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)
    
    return neighbors

# Example usage:
initial_state = [[1, 2, 3], [4, 0, 6], [7, 5, 8]]
solution = bfs_8puzzle(initial_state)
for step in solution:
    print(step)
