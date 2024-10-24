





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





def dfs_8puzzle(initial_state):
    goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    stack = [(initial_state, [])]      #is line ko deque me convert karna hai and same code bfs ho jaayega 
    visited = set()

    while stack:
        state, path = stack.pop() #pop the last element from the stack
        if state == goal_state:
            return path
        visited.add(tuple(map(tuple, state))) #add the state to visited
        for neighbor in get_neighbors(state): #get the neighbors of the current state
            if tuple(map(tuple, neighbor)) not in visited: #if the neighbor is not visited then add it to the stack
                stack.append((neighbor, path + [neighbor])) #add the neighbor to the stack and add the path to the neighbor
                
                
                

# Example usage:
initial_state = [[1, 2, 3], [4, 0, 6], [7, 5, 8]]
solution = dfs_8puzzle(initial_state)
for step in solution:
    print(step)
