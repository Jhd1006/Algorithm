import sys
input = sys.stdin.readline
from collections import deque

N, M , V = map(int, input().split())
adj = [[] for _ in range(N+1)]

for _ in range(M):
    v1, v2 = map(int, input().split())
    adj[v1].append(v2)
    adj[v2].append(v1)

for l in adj:
    l.sort()

vis = [False] * (N+1)
ans_d = []
def dfs(cur):
    vis[cur] = True
    ans_d.append(cur)
    for nxt in adj[cur]:
        if vis[nxt]:
            continue
        dfs(nxt)

ans_b = []
def bfs(V):
    vis = [False] * (N+1)
    vis[V] = True
    q = deque([V])
    while q:
        cur = q.popleft()
        ans_b.append(cur)
        for nxt in adj[cur]:
            if vis[nxt]:
                continue
            q.append(nxt)
            vis[nxt] = True

dfs(V)
bfs(V)
print(' '.join(map(str, ans_d)))
print(' '.join(map(str, ans_b)))