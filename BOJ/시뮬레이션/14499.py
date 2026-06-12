import sys
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

N, M, x, y, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
cmd = list(map(int, input().split()))

dice = [0]*7
# 1 2 3 4 5 6

# 동쪽 : 4 2 1 6 5 3
# 서쪽 : 3 2 6 1 5 4
# 남쪽 : 2 6 3 4 1 5
# 북쪽 : 5 1 3 4 6 2

def func(x, y, dir):
    nx = x+dx[dir]
    ny = y+dy[dir]
    if nx < 0 or nx >= N or ny < 0 or ny >= M:
        return x, y
    if dir == 0:
        dice[1], dice[3], dice[4], dice[6] = dice[4], dice[1], dice[6], dice[3]
    elif dir == 1:
        dice[1], dice[3], dice[4], dice[6] = dice[3], dice[6], dice[1], dice[4]
    elif dir == 2:
        dice[1], dice[2], dice[5], dice[6] = dice[5], dice[1], dice[6], dice[2]
    elif dir == 3:
        dice[1], dice[2], dice[5], dice[6] = dice[2], dice[6], dice[1], dice[5]
    if board[nx][ny] == 0:
        board[nx][ny] = dice[6]
    else:
        dice[6] = board[nx][ny]
        board[nx][ny] = 0
    print(dice[1])
    return nx, ny

    
for c in cmd:
    x, y = func(x, y, c-1)

0
0
0
3
0
1
0
6
0

0
0
0
8
0
6
0
1
0