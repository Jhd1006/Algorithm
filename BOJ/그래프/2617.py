import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
adj1 = [[] for _ in range(N+1)]
adj2 = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    adj1[u].append(v)
    adj2[v].append(u)

def bfs(adj, start):
    cnt = 0
    vis = [False]*(N+1)
    vis[start] = True
    q = deque([start])
    while q:
        cur = q.popleft()
        for nxt in adj[cur]:
            if vis[nxt]:
                continue
            cnt += 1
            vis[nxt] = True
            q.append(nxt)
    return cnt

ans = 0
for i in range(1, N+1):
    if max (bfs(adj1, i), bfs(adj2, i)) > N // 2:
        ans += 1
print(ans)
