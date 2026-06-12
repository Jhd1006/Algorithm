import sys
from collections import deque
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

N, M = map(int, input().split())

board = [list(map(int, input().strip())) for _ in range (N)]
dist = [[[-1] * 2 for _ in range(M)]for _ in range(N)]

dist[0][0][0] = 0
q = deque([(0, 0, 0)])

while q:
    x, y, b = q.popleft()
    if x == N-1 and y == M-1:
        print(dist[x][y][b] + 1)
        break
    for dir in range(4):
        nx = x + dx[dir]
        ny = y + dy[dir]
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if board[nx][ny] == 1 and b == 0:
            dist[nx][ny][1] = dist[x][y][b] + 1
            q.append((nx, ny, 1))
        elif board[nx][ny] == 0 and dist[nx][ny][b] == -1:
            dist[nx][ny][b] = dist[x][y][b] + 1
            q.append((nx,ny,b))
else:
    print(-1)