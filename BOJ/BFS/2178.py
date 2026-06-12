import sys
from collections import deque
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(n)]
dist = [[-1] * m for _ in range(n)]

q = deque([(0, 0)])
dist[0][0] = 1
while q:
    x, y = q.popleft()
    for dir in range(4):
        nx = x + dx[dir]
        ny = y + dy[dir]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if dist[nx][ny] != -1 or board[nx][ny] == 0:
            continue
        dist[nx][ny] = dist[x][y] + 1
        q.append((nx, ny))
print(dist[n-1][m-1])

