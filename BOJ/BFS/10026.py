import sys
from collections import deque
input = sys.stdin.readline
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N = int (input().strip())
board = [list(input().strip()) for _ in range(N)]
vis = [[False]* N for _ in range(N)]

def bfs(i, j) :
    q = deque([(i,j)]) 
    vis[i][j] = True
    color = board[i][j]
    while q:
        x, y = q.popleft()
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if vis[nx][ny] or color != board[nx][ny]:
                continue
            vis[nx][ny] = True
            q.append((nx,ny))

cnt = 0
cnt_rg = 0
for i in range(N):
    for j in range(N):
        if vis[i][j]:
            continue
        cnt += 1
        bfs(i,j)
for i in range(N):
    for j in range(N):
        vis[i][j] = False
        if board[i][j] =='G':
            board[i][j] = 'R'
for i in range(N):
    for j in range(N):
        if vis[i][j]:
            continue
        cnt_rg += 1
        bfs(i,j)          
print(str(cnt) + ' ' + str(cnt_rg))