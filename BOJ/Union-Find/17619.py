import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, Q = map(int, input().split())
p = [-1] * (100001)
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
    if p[v] == p[u]:
        p[u] -= 1
    p[v] = u
    return True

trees = []
for i in range(1, N+1):
    x1, x2, y = map(int, input().split())
    trees.append((x1, x2, i))
trees.sort()

mx = 0
for i in range(N-1):
    mx = max(mx, trees[i][1])
    if mx >= trees[i+1][0]:
        union(trees[i][2], trees[i+1][2])

ans = []
for _ in range(Q):
    a, b = map(int, input().split())
    if find(a) == find(b):
        ans.append('1')
    else:
        ans.append('0')

print('\n'.join(ans))