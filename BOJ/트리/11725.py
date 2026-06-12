import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
p = [0] * (N+1)
adj = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

def bfs(root):
    q = deque([root])
    while q:
        cur = q.popleft()
        for nxt in adj[cur]:
            if p[cur] == nxt:
                continue
            q.append(nxt)
            p[nxt] = cur
bfs(1)
for x in p[2:]:
    print(x)

