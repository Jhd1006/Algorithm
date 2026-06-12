import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
adj = [[] for _ in range(N+1)]


def bfs(start, end):
    q = deque([(start, 0)])
    dist = 0
    while q:
        cur, dist = q.popleft()
        if cur == end:
            return dist
        for nxt, d in adj[cur]:
            if p[cur] == nxt:
                continue
            p[nxt] = cur
            q.append((nxt, dist + d))


for _ in range(N-1):
    u, v, d = map(int, input().split())
    adj[u].append((v, d))
    adj[v].append((u, d))

ans=[]
for _ in range(M):
    p = [0] * (N+1)
    x, y = map(int, input().split())
    ans.append(str(bfs(x, y)))

print('\n'.join(ans))



