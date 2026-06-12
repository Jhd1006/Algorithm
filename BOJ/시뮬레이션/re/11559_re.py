import sys
input = sys.stdin.readline
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

field = [list(input().strip()) for _ in range(12)]

def down():
    for j in range(6):
        puyos = deque()
        for i in range(11, -1, -1):
            if field[i][j] == '.':
                continue
            puyos.append(field[i][j])
            field[i][j] = '.'
        idx = 11
        while puyos:
            field[idx][j] = puyos.popleft()
            idx -= 1

def puyo(x, y):
    q = deque([(x, y)])
    exploded = []
    exploded.append((x, y))
    vis[x][y] = True
    while q:
        qx, qy = q.popleft()
        for dir in range(4):
            nx = qx + dx[dir]
            ny = qy + dy[dir]
            if nx < 0 or nx >= 12 or ny < 0 or ny >= 6:
                continue
            if vis[nx][ny] or field[nx][ny] != field[qx][qy]:
                continue
            q.append((nx, ny))
            vis[nx][ny] = True
            exploded.append((nx, ny))
    if len(exploded) >= 4:
        for ex, ey in exploded:
            field[ex][ey] = '.'
        return True
    return False

cnt = 0
while True:
    vis = [[False] * 6 for _ in range(12)]
    chain = False
    down()
    for i in range(12):
        for j in range(6):
            if field[i][j] == '.' or vis[i][j]:
                continue
            if puyo(i,j):
                chain = True   
    if not chain:
        break
    cnt += 1
print(cnt)
