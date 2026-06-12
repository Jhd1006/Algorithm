import sys
input = sys.stdin.readline

V = int(input())
E = int(input())

adj = [[] for _ in range(V+1)]
vis = [False] * (V+1)

for _ in range(E):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

cnt = 0
def dfs(cur):
    global cnt
    vis[cur] = True
    for nxt in adj[cur]:
        if vis[nxt]:
            continue
        cnt += 1
        dfs(nxt)

dfs(1)
print(cnt)

