import sys
from collections import deque
input = sys.stdin.readline
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
ans = []

T = int(input().strip())
for _ in range(T):
    M, N, K = map(int, input().split())
    board = [[0] * M for _ in range(N)]
    vis = [[False] * M for _ in range(N)]

    for _ in range(K):
        X, Y = map(int, input().split())
        board[Y][X] = 1
    
    def bfs (a, b):
        Q = deque([(a,b)])
        vis[a][b] = True
        while Q:
            x, y = Q.popleft()
            for dir in range(4):
                nx = x + dx[dir]
                ny = y + dy[dir]
                if nx < 0 or nx >= N or ny < 0 or ny >= M:
                    continue
                if vis[nx][ny] or board[nx][ny] == 0:
                    continue
                Q.append((nx,ny))
                vis[nx][ny] = True
    cnt = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0 or vis[i][j]:
                continue
            cnt += 1
            bfs(i,j)
    ans.append(cnt)

print('\n'.join(map(str, ans)))