import sys
input = sys.stdin.readline
from collections import deque

board = [list(input().strip()) for _ in range(12)]
vis = [[False] * 6 for _ in range(12)] 

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def puyo(a, b):
    exploded = []
    q = deque()
    q.append((a, b))
    exploded.append((a, b))
    vis[a][b] = True
    while q:
        x, y = q.popleft()
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if nx < 0 or nx >= 12 or ny < 0 or ny >= 6:
                continue
            if board[nx][ny] != board[x][y] or vis[nx][ny]:
                continue 
            vis[nx][ny] = True
            q.append((nx, ny))   
            exploded.append((nx, ny))
    if len(exploded) >= 4:
        for tx, ty in exploded:
            board[tx][ty] = '.'
        return True
    return False

def down():
    for j in range(6):
        S = deque()
        for i in range(11, -1, -1):
          if board[i][j] != '.':
              S.append(board[i][j])  
              board[i][j] = '.'
        idx = 11
        while S:
            board[idx][j] = S.popleft()
            idx -= 1

cnt = 0

while True:
    vis = [[False] * 6 for _ in range(12)]
    chain = False
    down()
    for i in range(12):
        for j in range(6):
            if vis[i][j] or board[i][j] == '.':
                continue
            if puyo(i, j):
                chain = True
    if not chain:
        break
    cnt += 1
print(cnt)
    