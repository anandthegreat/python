def check_winner(board):
    n = len(board)
    
    # check horizontally
    for i in range(n):
        row_sum = 0
        for j in range(n):
            if board[i][j] == 'X':
                row_sum +=1
            elif board[i][j] == '0':
                row_sum -=1
        if row_sum == n:
            return ('game_over', 'X', 'horizontally')
        elif row_sum == -n:
            return ('game_over', '0','horizontally')
    
    
    # check vertically
    for i in range(n):
        col_sum = 0
        for j in range(n):
            if board[j][i] == 'X':
                col_sum += 1
            elif board[j][i] == '0':
                col_sum -= 1
        if col_sum == n:
            return ('game_over', 'X','vertically')
        elif col_sum == -n:
            return ('game_over', '0','vertically')
    
    # check diagonally
    diag_sum = 0
    for i in range(n):
        if board[i][i] == 'X':
            diag_sum += 1
        elif board[i][i] == '0':
            diag_sum -= 1
    if diag_sum == n:
        return ('game_over', 'X','diagonally')
    elif diag_sum == -n:
        return ('game_over', '0','diagonally')
        
    # check anti-diagonally
    diag_sum = 0
    for i in range(n-1,-1,-1):
        if board[n-i-1][i] == 'X':
            diag_sum += 1
        elif board[n-i-1][i] == '0':
            diag_sum -= 1
    if diag_sum == n:
        return ('game_over', 'X','anti-diagonally')
    elif diag_sum == -n:
        return ('game_over', '0','anti-diagonally')
    
    return ('in_progress', None)


board = [['X','',''],['','X',''],['0','0','X']] # diagonally X wins
print(check_winner(board))

board = [['0','','X'],['','X',''],['X','0','0']] # anti-diagonally X wins
print(check_winner(board))

board = [['X','',''],['','X',''],['0','0','0']] # horizontally 0 wins
print(check_winner(board))

board = [['0','',''],['0','X',''],['0','X','X']] # vertically 0 wins
print(check_winner(board))

board = [['X','',''],['','X',''],['0','0','']] # in_progress
print(check_winner(board))
            
            
            
            
            
            
