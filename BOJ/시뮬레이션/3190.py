import sys
input = sys.stdin.readline
from collections import deque
#동 북 서 남
# 오 위 왼 아 
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

N = int(input().strip())
K = int(input().strip())
board = [[0]*N for _ in range(N)]

dir = 0
# 1 : 사과 2 : 뱀
for _ in range(K):
    x, y = map(int, input().split())
    board[x-1][y-1] = 1

L = int(input().strip())
x, y = 0, 0
board[x][y] = 2
time = 0
cmd = deque()
tail = deque([(0, 0)])
tx, ty = 0, 0
for _ in range(L):
    X, C = input().split()
    cmd.append((int(X), C))
while True:
    time += 1
    nx = x + dx[dir]
    ny = y + dy[dir]
    if nx < 0 or nx >= N or ny < 0 or ny >= N or board[nx][ny] == 2:
        break
    if board[nx][ny] == 0:
        tx, ty = tail.popleft()
        board[tx][ty] = 0
    board[nx][ny] = 2
    x, y = nx, ny
    tail.append((nx, ny))
    if cmd and time == cmd[0][0]:
        X, C = cmd.popleft()
        if C == 'L':
            dir = (dir+1) % 4
        elif C == 'D':
            dir = (dir+3) % 4
    

print(time)
    