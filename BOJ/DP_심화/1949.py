import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())

adj = [[] for _ in range(N+1)]
p = [0] + list(map(int, input().split()))
d1 = [0] * (N+1)
d2 = [0] * (N+1)

for _ in range(N-1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

def dfs(cur, par):
    d1[cur] = p[cur]
    d2[cur] = 0
    for nxt in adj[cur]:
        if par == nxt:
            continue
        dfs(nxt, cur)
        d1[cur] += d2[nxt]
        d2[cur] += max(d1[nxt], d2[nxt])

dfs(1, 0)
print(max(d1[1], d2[1]))