import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n, m = map(int, input().split())
p = list(map(int, input().split())) + [0]
adj = [[] for _ in range(n+1)]
compliment = [0] * (n+1)
ans = [0] * (n+1)

def dfs(cur, com):
    ans[cur] = com
    for nxt in adj[cur]:
        p[nxt] = cur
        nxt_com = com + compliment[nxt]
        dfs(nxt, nxt_com)

for i in range(n):
    if p[i] >= 1:
        adj[p[i]].append(i+1)


for _ in range(m):
    i, w = map(int, input().split())
    compliment[i] += w

dfs(1, compliment[1])
print(' '.join(map(str, ans[1:])))



