import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())

adj = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

def bfs(start):
    dist = [-1] * (N+1)
    q = deque([start])
    dist[start] = 0
    while q:
        cur = q.popleft()
        for nxt in adj[cur]:
            if dist[nxt] != -1:
                continue
            dist[nxt] = dist[cur] + 1
            q.append(nxt)
    return sum(dist)

kevin = []
for i in range(1, N+1):
    kevin.append(bfs(i))
mn = min(kevin)

print(kevin.index(mn)+1)



