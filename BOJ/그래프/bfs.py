import sys
input = sys.stdin.readline
from collections import deque

adj = [[] for _ in range(10)]

dist = [-1] * 10

def bfs():
    vis = [False] * 10
    q = deque()
    q.append(1)
    vis[1] = True
    while q:
        cur = q.popleft()
        print(cur)
        for nxt in adj[cur]:
            if vis[nxt]:
                continue
            q.append(nxt)
            vis[nxt] = True

vis = [False] * 10
def dfs(cur):
    vis[cur] = True
    print(cur)
    for nxt in adj[cur]:
        if vis[nxt]:
            continue
        dfs(nxt)



def get_distance(start, end):
    q = deque([start])
    dist[start] = 0
    while q:
        cur = q.popleft()
        for nxt in adj[cur]:
            if dist[nxt] != -1:
                continue
            q.append(nxt)
            dist[nxt] = dist[cur] + 1
    print(dist[end])

edges = [(1, 2), (1, 3), (2, 4), (2, 5), (5, 6)]

for u, v in edges:
    adj[u].append(v)
    adj[v].append(u) 

bfs()
get_distance(1,6)
dfs(1)
