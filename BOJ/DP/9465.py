import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0]*n for _ in range(2)]
    if n == 1:
        print(max(board[0][0], board[1][0]))
        continue

    dp[0][0], dp[1][0] = board[0][0], board[1][0]

    for i in range(2):
        dp[i][1] = dp[1-i][0] + board[i][1]
    for i in range(2, n):
        for j in range(2):
            dp[j][i] = max(dp[1-j][i-1], dp[1-j][i-2]) + board[j][i]
            
    print(max(dp[1][n-1], dp[0][n-1]))
    
