import sys
from collections import deque
input = sys.stdin.readline
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
vis = [[False] * m for _ in range(n)]

def bfs(i, j):
    q = deque([(i,j)])
    vis[i][j] = True
    area = 1
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
            area += 1
            q.append((nx, ny))
    return area

if __name__ == "__main__":
    cnt = 0
    mx = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1 and not vis[i][j]:
                cnt += 1
                mx = max(mx, bfs(i,j))
    print(cnt)
    print(mx)