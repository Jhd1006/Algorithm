import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
adj = [[] for _ in range(N+1)]
deg = [0] * (N+1)
result = []

for _ in range(M):
    l = list(map(int, input().split()))
    for i in range(1, l[0]):
        adj[l[i]].append(l[i+1])
        deg[l[i+1]] += 1

q = deque()

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

if len(result) != N:
    print(0)
else:         
    print('\n'.join(map(str, result)))