import sys
input = sys.stdin.readline

dx = [1, 0, -1, 0] #남 동 북 서
dy = [0, 1, 0, -1]

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
changed = [[0]*M  for _ in range(N)]
# 동 동서 동북 동북서 동북서남

def change(x, y, dir):
    dir %= 4
    while True:
        x = x + dx[dir]
        y = y + dy[dir]
        if x < 0 or x >= N or y < 0 or y >= M:
            return
        if board[x][y] == 6:
            return
        if board[x][y] != 0:
            continue
        changed[x][y] = '#'

cctv = []
empty = 0
for i in range(N):
    for j in range(M):
        if board[i][j] != 0 and board[i][j] != 6:
            cctv.append((i, j)) 
        if board[i][j] == 0:
            empty += 1

for tmp in range(1 << (2*len(cctv))):
    changed = [row[:] for row in board]
    brute = tmp
    for i in range(len(cctv)):
        dir = brute % 4
        brute //= 4
        x, y = cctv[i]
        if board[x][y] == 1:
            change(x, y, dir)
        elif board[x][y] == 2:
            change(x, y, dir)
            change(x, y, dir+2)
        elif board[x][y] == 3:
            change(x, y, dir)
            change(x, y, dir+1)
        elif board[x][y] == 4:
            change(x, y, dir)
            change(x, y, dir+1)
            change(x, y, dir+2)
        else:
            change(x, y, dir)
            change(x, y, dir+1)
            change(x, y, dir+2)
            change(x, y, dir+3)
    cnt = 0
    for i in range(N):
        for j in range(M):
            if changed[i][j] == 0:
                cnt += 1
    empty = min(empty, cnt)
print(empty)
