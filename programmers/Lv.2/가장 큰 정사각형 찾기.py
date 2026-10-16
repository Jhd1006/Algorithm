def solution(board):
    answer = 1234
    w, h = len(board[0]), len(board)
    mx = 0
    
    for i in range(h):
        for j in range(w):
            if board[i][j] == 1:
                mx = 1
                
    for i in range(1, h):
        for j in range(1, w):
            if board[i][j] == 1:
                board[i][j] = min(board[i-1][j], board[i][j-1], board[i-1][j-1]) + 1
                mx = max(mx, board[i][j])
                
    answer = mx ** 2
    
    return answer
