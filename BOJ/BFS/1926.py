import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
result = []
vis = [[False] * m for _ in range(n)]
cnt = 0
mx = 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
    for j in range(m):
        if board[i][j] == 0 or vis[i][j]:
            continue
        q = deque([(i,j)])
        vis[i][j] = True
        area = 1
        cnt += 1
        while q:
            x, y = q.popleft()
            for dir in range(4):
                nx = x + dx[dir]
                ny = y + dy[dir]
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                     continue
                if vis[nx][ny] or board[nx][ny] == 0:
                    continue
                vis[nx][ny] = True
                q.append((nx, ny))
                area += 1
        mx = max(mx, area)

print(cnt)
print(mx)
                
