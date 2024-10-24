from heapq import heappush, heappop

def simple_tictactoe_ai(board, player):
    def is_winner(board, player):
        # Check rows, columns and diagonals
        for i in range(3):
            if all(board[i][j] == player for j in range(3)) or \
               all(board[j][i] == player for j in range(3)):
                return True
        return all(board[i][i] == player for i in range(3)) or \
               all(board[i][2-i] == player for i in range(3))
    
    def get_moves(board):
        return [(i, j) for i in range(3) 
                for j in range(3) if board[i][j] == 0]
    
    best_move = None
    
    for i, j in get_moves(board):
        # Make move
        new_board = [row[:] for row in board]
        new_board[i][j] = player
        
        if is_winner(new_board, player):
            return new_board
        
        # Store first valid move
        if best_move is None:
            best_move = new_board
    
    return best_move or board

# Example usage:
board = [
    [1, 0, -1],
    [0, 1, 0],
    [0, 0, 0]
]

next_move = simple_tictactoe_ai(board, 2)
for row in next_move:
    print(row)
