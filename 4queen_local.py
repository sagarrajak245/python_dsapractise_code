def conflicts(board, row, col):
    hits = 0
    for i in range(len(board)):
        if i == row:
            continue
        if board[i] == col or \
           abs(board[i] - col) == abs(i - row):
            hits += 1
    return hits

def print_solution(board):
    solution = []
    for i in range(len(board)):
        row = ['.'] * len(board)
        row[board[i]] = 'Q'
        solution.append(''.join(row))
    return solution

def total_conflicts(board):
    total = 0
    for i in range(len(board)):
        total += conflicts(board, i, board[i])
    return total // 2

def hill_climbing(n):
    # Initialize board
    board = list(range(n))
    current_conflicts = total_conflicts(board)
    
    while current_conflicts > 0:
        improved = False
        for col in range(n):
            original_pos = board[col]
            
            for row in range(n):
                if row != original_pos:
                    board[col] = row
                    new_conflicts = total_conflicts(board)
                    
                    if new_conflicts < current_conflicts:
                        current_conflicts = new_conflicts
                        improved = True
                        break
                    else:
                        board[col] = original_pos
                        
            if improved:
                break
                
        if not improved:
            break
    
    solution = print_solution(board)
    return [solution]  # Return list of solutions to match format

# Example Usage
if __name__ == "__main__":
    print("Hill Climbing Solutions:")
    hill_climbing_solutions = hill_climbing(4)
    for sol in hill_climbing_solutions:
        for row in sol:
            print(row)
        print()