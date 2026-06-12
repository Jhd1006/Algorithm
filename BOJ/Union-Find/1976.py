import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
M = int(input())
p = [-1] * (N+1)
# for _ in range(N):
adj = [list(map(int, input().split())) for _ in range(N)]
plan = list(map(int, input().split()))

def find(x):
    if p[x] < 0:
        return x
    p[x] = find(p[x])
    return p[x]

def union(u, v):
    u = find(u)
    v = find(v)
    if u == v:
        return False
    if p[v] < p[u]:
        u, v = v, u
    if p[u] == p[v]:
        p[u] -= 1
    p[v] = u
    return True

def isOK(arr):
    for i in range(M-1):
        if find(plan[i]) != find(plan[i+1]):
            return False
    return True

for i in range(N):
    for j in range(N):
        if adj[i][j]:
            union(i+1, j+1)

if isOK(plan):
    print("YES")
else:
    print("NO")
    
