def is_safe(board, row, col):
    # Check if there's a queen in the same row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens_util(board, col):
    if col >= len(board):
        return True

    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1

            if solve_n_queens_util(board, col + 1):
                return True

            board[i][col] = 0

    return False

def solve_n_queens(N):
    board = [[0] * N for _ in range(N)]

    if not solve_n_queens_util(board, 0):
        print("No solution exists")
        return

    print("Solution:")
    for row in board:
        print(' '.join(map(str, row)))

# Example usage:
n = 5
solve_n_queens(n)
