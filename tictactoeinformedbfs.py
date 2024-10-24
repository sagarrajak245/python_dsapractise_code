def simple_tictactoe_ai(board, player):
    # Convert 2D board to 1D for easier processing
    flat_board = [cell for row in board for cell in row]
    
    def is_winner(board):
        # Check rows, columns, and diagonals for a win
        lines = [
            board[0:3], board[3:6], board[6:9],  # Rows
            board[0:9:3], board[1:9:3], board[2:9:3],  # Columns
            board[0:9:4], board[2:7:2]  # Diagonals
        ]
        return any(line.count(player) == 3 for line in lines)   # if any line has 3 same elements then return True
    
    # Get available moves
    moves = [i for i in range(9) if flat_board[i] == 0]
    
    # Check for a winning move
    for move in moves:
        new_board = flat_board[:]
        new_board[move] = player  # Make the move
        if is_winner(new_board):
            return to_2d(new_board)
    
    # If no winning move, make the first available move
    if moves:
        new_board = flat_board[:]
        new_board[moves[0]] = player  # Make the first available move
        return to_2d(new_board)
    
    # If no moves available, return the original board
    return board


 


def to_2d(flat_board):
    return [flat_board[i:i+3] for i in (0, 3, 6)]

# Example usage
board = [
    [1, 0, -1],
    [0, 1, 0],
    [0, 0, 0]
]
next_move = simple_tictactoe_ai(board, 1)
for row in next_move:
    print(row)
