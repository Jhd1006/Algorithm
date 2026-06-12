import sys
from collections import deque
input = sys.stdin.readline
MX = 100001
dx = [-1, 1]
N, K = map(int, input().split())
dist = [-1] * MX
dist[N] = 0
q = deque()
q.append(N)
while q:
    x = q.popleft()
    if x == K:
        print(dist[x])
        break

    # 0-1 BFS
    # 순간이동의 경우 좌우 이동보다 우선도 높으므로 먼저 수행 (가중치 0)
    if 2*x < MX and dist[2*x] == -1:  
        dist[2*x] = dist[x]
        q.appendleft(2*x)  #우선도 높으니 앞에 넣음

    for dir in range(2):
        nx = x + dx[dir]
        if nx < 0 or nx >= MX or dist[nx] != -1:
            continue
        dist[nx] = dist[x] + 1
        q.append(nx)

