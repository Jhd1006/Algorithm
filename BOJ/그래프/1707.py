import sys
input = sys.stdin.readline
from collections import deque
K = int(input())

def isBipartite(V):
    color = [0] * (V+1)
    for i in range(1, V+1):
        if color[i] != 0:
            continue
        q = deque([i])
        color[i] = 1
        while q:
            cur = q.popleft()
            for nxt in adj[cur]:
                if color[nxt] == color[cur]:
                    return False
                elif color[nxt] != 0:
                    continue
                color[nxt] = -color[cur]
                q.append(nxt)
    return True

ans = []
for _ in range(K):
    V, E = map(int, input().split())
    adj = [[] for _ in range(V+1)]
    for _ in range(E):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    if isBipartite(V):
        ans.append("YES")
    else:
        ans.append("NO")

print('\n'.join(ans))