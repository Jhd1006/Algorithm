import sys
input = sys.stdin.readline
from collections import deque
from itertools import combinations
# 0 빈칸 1 벽 2 바이러스 

dx= [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

def bfs():
    global mboard
    q = deque(virus)
    while q:
        x, y = q.popleft()
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if mboard[nx][ny] == 0:
                mboard[nx][ny] = 2
                q.append((nx, ny))
            
empty = []
virus = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            empty.append((i, j))
        elif board[i][j] == 2:
            virus.append((i, j))

comb = combinations(empty, 3)

mx = 0
for c in comb:
    mboard = [row[:] for row in board]
    for i, j in c:
        mboard[i][j] = 1
    bfs()
    cnt = sum(row.count(0) for row in mboard)
    mx = max(mx, cnt)

print(mx)

