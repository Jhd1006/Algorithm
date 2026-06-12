import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
adj = [[] for _ in range(N+1)]
deg = [0] * (N+1)

for _ in range(M):
    A, B = map(int, input().split())
    adj[A].append(B)
    deg[B] += 1

q = deque()
result = []

for i in range(1, N+1):
    if deg[i] == 0:
        q.append(i)

while q:
    cur = q.popleft()
    result.append(cur)
    for nxt in adj[cur]:
        deg[nxt] -= 1
        if deg[nxt] == 0:
            q.append(nxt)

print(' '.join(map(str, result)))



