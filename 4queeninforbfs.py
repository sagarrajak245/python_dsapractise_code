

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


def heuristic(board):
    return len(board)







def informed_bfs(n):
    from queue import PriorityQueue
    pq = PriorityQueue()
    pq.put((0, 0, []))  # (priority, row, board)
    solutions = []
    
    while not pq.empty():
        priority, row, board = pq.get()
        if row == n:
            solutions.append(print_solution(board))
        else:
            for col in range(n):
                if is_safe(board, row, col):
                    pq.put((heuristic(board), row + 1, board + [col]))
    return solutions

# Example Usage
if __name__ == "__main__":
    print("Informed BFS Solutions:")
    informed_bfs_solutions = informed_bfs(4)
    for sol in informed_bfs_solutions:
        for row in sol:
            print(row)
        print()
