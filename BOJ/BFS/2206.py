import sys
from collections import deque
input = sys.stdin.readline
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N , M = map(int, input().split()) 
board = [list(map(int,input().strip())) for _ in range(N)]
dist = [[[-1]*2 for _ in range(M)] for _ in range(N)]
q = deque([(0, 0, 0)])
## dist[0][0][k] k가 1이면 부숨 0이면 아직 안 부숨
dist[0][0][0] = 1
isSuccess = False
while q:
    x, y, b = q.popleft()
    if x == N - 1 and y == M - 1 :
        isSuccess = True
        ans = dist[x][y][b]
        break
    for dir in range(4):
        nx = x + dx[dir]
        ny = y + dy[dir]
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if board[nx][ny] == 0 and dist[nx][ny][b] == -1: ## 다음 칸이 비었고 방문 안함
            dist[nx][ny][b] = dist[x][y][b] + 1
            q.append((nx, ny, b))
        elif board[nx][ny] == 1 and b == 0:              ## 다음 칸이 벽이고 아직 안부숨
            dist[nx][ny][1] = dist[x][y][b] + 1
            q.append((nx, ny, 1))
print(ans if isSuccess else -1)


# import sys
# from collections import deque
# input = sys.stdin.readline

# dx = [1, 0, -1, 0]
# dy = [0, 1, 0, -1]
# N, M = map(int, input().split())
# board = [list(map(int, input().strip())) for _ in range(N)]

# dist = [[[-1] * 2 for _ in range(M)]  for _ in range(N)]
# q = deque([(0, 0, 0)])
# dist[0][0][0] = 1

# while q:
#     x, y, b = q.popleft()
#     if x == N-1 and y == M-1:
#         print(dist[x][y][b])
#         break
#     for dir in range(4):
#         nx = x + dx[dir]
#         ny = y + dy[dir]
#         if nx < 0 or nx >= N or ny < 0 or ny >= M:
#             continue
#         if board[nx][ny] == 0 and dist[nx][ny][b] == -1:
#             q.append((nx, ny, b))
#             dist[nx][ny][b] = dist[x][y][b] + 1
#         if board[nx][ny] == 1 and b == 0:
#             q.append((nx, ny, 1))
#             dist[nx][ny][1] = dist[x][y][b] + 1
# else:
#     print(-1)