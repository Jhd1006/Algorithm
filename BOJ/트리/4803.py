import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from collections import deque

def dfs(cur, par):
    global isTree
    for nxt in adj[cur]:
        if par == nxt:
            continue
        if vis[nxt]:
            isTree = False
            continue
        vis[nxt] = True
        dfs(nxt, cur)

test_case = 0
ans = []
while True:
    test_case += 1
    n, m = map(int, input().split())
    vis = [False] * (n+1)
    adj = [[] for _ in range(n+1)]
    cnt = 0
    if (n, m) == (0, 0):
        break
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    for i in range(1, n+1):
        if vis[i]:
            continue
        vis[i] = True
        isTree = True
        dfs(i, 0)
        if isTree:
            cnt += 1
    print(f"Case {test_case}: ", end ='')
    if cnt == 0:
        print("No trees.")
    elif cnt == 1:
        print("There is one tree.")
    else:
        print(f"A forest of {cnt} trees.")




