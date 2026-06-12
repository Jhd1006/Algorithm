import sys
from collections import deque
input = sys.stdin.readline
dx = [1, 0, 0, -1, 0, 0]
dy = [0, 1, 0, 0, -1, 0]
dz = [0, 0, 1, 0, 0, -1]
M, N, H = map(int, input().split())

board = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
dist= [[[-1] * M for _ in range(N)] for _ in range(H)]
Q = deque()

for i in range(H):
    for j in range(N):
        for k in range(M):
            if board[i][j][k] == 1:
                Q.append((i, j, k))
                dist[i][j][k] = 0

while Q:
    z, x, y = Q.popleft()
    for dir in range(6):
        nx = x + dx[dir]
        ny = y + dy[dir]
        nz = z + dz[dir]
        if nz < 0 or nz >= H or nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if dist[nz][nx][ny] != -1 or board[nz][nx][ny] != 0:
            continue
        dist[nz][nx][ny] = dist[z][x][y] + 1
        Q.append((nz, nx, ny))

mx = 0
isFailed = False
for i in range(H):
    for j in range(N):
        for k in range(M):
            if dist[i][j][k] == -1 and board[i][j][k] == 0:
                isFailed = True
            mx = max(mx, dist[i][j][k])

if isFailed:
    print(-1)
else:
    print(mx)