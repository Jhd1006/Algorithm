import sys
input = sys.stdin.readline

N = int(input().strip())
board = [list(map(int, input().split())) for _ in range(N)]
cost = [[0] * 3 for _ in range(N)]
for i in range(3):
    cost[0][i] = board[0][i]
for i in range(1, N):
    cost[i][0] = min(cost[i-1][1], cost[i-1][2]) + board[i][0]
    cost[i][1] = min(cost[i-1][0], cost[i-1][2]) + board[i][1]
    cost[i][2] = min(cost[i-1][0], cost[i-1][1]) + board[i][2]

mn = min(cost[N-1])
print(mn)
