def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def print_solution(board):
    solution = []
    for i in range(len(board)):
        row = ['.'] * len(board)
        row[board[i]] = 'Q'
        solution.append(''.join(row))
    return solution

def heuristic(board, n):
    # Estimate remaining conflicts
    remaining_queens = n - len(board)
    return remaining_queens

def a_star(n):
    from queue import PriorityQueue
    pq = PriorityQueue()
    pq.put((0, 0, []))  # (f_score, row, board)
    solutions = []
    
    while not pq.empty():
        f_score, row, board = pq.get()
        
        if row == n:
            solutions.append(print_solution(board))
        else:
            for col in range(n):
                if is_safe(board, row, col):
                    new_board = board + [col]
                    g = len(new_board)  # Cost so far
                    h = heuristic(new_board, n)  # Estimated remaining cost
                    f = g + h  # A* f-score
                    pq.put((f, row + 1, new_board))
    return solutions

# Example Usage
if __name__ == "__main__":
    print("A* Solutions:")
    a_star_solutions = a_star(4)
    for sol in a_star_solutions:
        for row in sol:
            print(row)
        print()