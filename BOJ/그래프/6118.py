import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
adj = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())
    adj[A].append(B)
    adj[B].append(A)

dist = [-1] * (N+1)
dist[1] = 0
q = deque([1])
while q:
    cur = q.popleft()
    for nxt in adj[cur]:
        if dist[nxt] != -1:
            continue
        dist[nxt] = dist[cur] + 1
        q.append(nxt)

mx = max(dist)
result = [(i, v) for i, v in enumerate(dist) if v == mx]
print(result[0][0], result[0][1], len(result))