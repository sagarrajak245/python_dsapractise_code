def solve_4puzzle_simple(initial, goal):
    def manhattan(state):
        # Simplified Manhattan distance calculation
        distance = 0
        for i in range(4):
            if state[i] != 0 and state[i] != goal[i]:
                curr_pos = i
                goal_pos = goal.index(state[i])
                # Convert to 2D coordinates
                curr_row, curr_col = curr_pos // 2, curr_pos % 2
                goal_row, goal_col = goal_pos // 2, goal_pos % 2
                distance += abs(curr_row - goal_row) + abs(curr_col - goal_col)
        return distance
    
    def get_moves(state):
        # Get possible moves from current state
        moves = []
        blank = state.index(0)
        row, col = blank // 2, blank % 2
        
        # Try all possible moves: up, down, left, right
        for nrow, ncol in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
            if 0 <= nrow < 2 and 0 <= ncol < 2:
                new_state = state[:]
                swap_pos = nrow * 2 + ncol
                new_state[blank], new_state[swap_pos] = new_state[swap_pos], new_state[blank]
                moves.append(new_state)
        return moves
    
    # Convert 2D to 1D for simpler operations
    current = [tile for row in initial for tile in row]
    goal = [tile for row in goal for tile in row]
    best_distance = manhattan(current)
    
    # Keep trying until no better move is found
    while True:
        improved = False
        for next_state in get_moves(current):
            next_distance = manhattan(next_state)
            if next_distance < best_distance:
                current = next_state
                best_distance = next_distance
                improved = True
                break
        
        if not improved or best_distance == 0:
            break
    
    # Convert back to 2D for display
    return [current[i:i+2] for i in (0,2)], best_distance

# Example usage
initial = [
    [1, 2],
    [0, 3]
]
goal = [
    [1, 2],
    [3, 0]
]

solution, distance = solve_4puzzle_simple(initial, goal)
print("Solution:")
for row in solution:
    print(row)
print(f"Distance: {distance}")