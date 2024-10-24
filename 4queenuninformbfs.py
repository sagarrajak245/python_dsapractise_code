
def is_safe(board,row,col):
    for i in range(row):
        if board[i]==col or\
            board[i]-i== col-row or \
            board[i]+i==col+row :
                return False
             
    return True   

def print_sol(board):
    solutions=[]
    for i in range(len(board)):
        row='.'*len(board)
        row[board[i]]= 'Q'
        solutions.append("".join(row))
    return solutions
        





def bfs(n):
    queue=[(0,[])]
    solutions=[]
    
    while queue:
        row ,board=queue.pop()
        
        if row==n:
            solutions.append(print_sol(board))
        else:
            
            for col in range (n):
                if is_safe(board,row,col):
                    queue.append((row+1, board+[col]))
                 
    return solutions 










if __name__=='__main__':
    print ("bfs soution")
    bfs_sol=bfs(4)
    for sol in bfs_sol:
        for row in sol:
            print(row)
        print()
    
    
    