from heapq import heappop, heappush



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

def manhattan(state):
    goal_positions = {1: (0, 0), 2: (0, 1), 3: (0, 2), 4: (1, 0), 5: (1, 1), 6: (1, 2), 7: (2, 0), 8: (2, 1)}
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                goal_x, goal_y = goal_positions[state[i][j]]
                distance += abs(goal_x - i) + abs(goal_y - j)
    return distance





def informed_bfs_8puzzle(initial_state):
    goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    pq = [(0, initial_state, [])]
    visited = set()

    while pq:
        _, state, path = heappop(pq)
        if state == goal_state:
            return path
        visited.add(tuple(map(tuple, state)))
        for neighbor in get_neighbors(state):
            if tuple(map(tuple, neighbor)) not in visited:
                heappush(pq, (manhattan(neighbor), neighbor, path + [neighbor])) 

# Example usage:
initial_state = [[1, 2, 3], [4, 0, 6], [7, 5, 8]]
solution = informed_bfs_8puzzle(initial_state)
for step in solution:
    print(step)
