import sys
input = sys.stdin.readline
from collections import deque
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
adj = [[] for _ in range(N+1)]
vis = [False] * (N+1)

for _ in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

def dfs(cur):
    vis[cur] = True
    for nxt in adj[cur]:
        if vis[nxt]:
            continue
        dfs(nxt)

cnt = 0
for i in range(1, N+1):
    if vis[i]:
        continue
    cnt += 1
    dfs(i)

print(cnt)
# def bfs(start):
#     cnt = 0
#     q = deque()
#     for i in range(1, N+1):
#         if vis[i]:
#             continue
#         cnt += 1
#         vis[i] = True
#         q.append(i)
#         while q:
#             cur = q.popleft()
#             for nxt in adj[cur]:
#                 if vis[nxt]:
#                     continue
#                 q.append(nxt)
#                 vis[nxt] = True
#     return cnt

# print(bfs(1))


