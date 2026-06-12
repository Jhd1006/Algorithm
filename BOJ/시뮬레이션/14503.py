import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# d 0, 1, 2, 3 : 북, 동, 남, 서
# board 0이면 청소안됨, 1이면 벽
x, y = r, c
dir = d

if board[x][y] == 0:
    board[x][y] = 2

while True:
    moved = False
    for _ in range(4):
        dir = (dir+3) % 4
        nx = x + dx[dir]
        ny = y + dy[dir]
        if board[nx][ny] == 0:
            board[nx][ny] = 2
            x, y = nx, ny
            moved = True
            break
    if moved:
        continue
    bdir = (dir+2) % 4
    bx = x + dx[bdir]
    by = y + dy[bdir]
    if board[bx][by] == 1:
        break
    else:
        x, y = bx, by

cnt = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 2:
            cnt += 1
            
print(cnt)