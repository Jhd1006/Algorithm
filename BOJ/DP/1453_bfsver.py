import sys
input = sys.stdin.readline
from collections import deque
dx = [3, 2, 1]
dist = [0]*1000001
q = deque()
q.append(1)
N = int(input().strip())
while q:

    x = q.popleft()
    for move in range(3):
        if move == 2:
            nx = x + dx[move]
        else:
            nx = x * dx[move]
        if nx < 0 or nx >= 1000001 or dist[nx] != 0:
            continue
        dist[nx] = dist[x] +1
        q.append(nx)

print(dist[N])

