
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




def dfs(n):
    stack = [(0, [])]  # (row, board)  bas yaha queue ka diya to bfs ban jaayega 
    solutions = []
    
    while stack:
        row, board = stack.pop()
        if row == n:
            solutions.append(print_solution(board))
        else:
            for col in range(n):
                if is_safe(board, row, col):
                    stack.append((row + 1, board + [col]))
    return solutions

# Example Usage

print("dFS Solutions:")
dfs_solutions = dfs(4)
for sol in dfs_solutions:
    for row in sol:
        print(row)
        print()
