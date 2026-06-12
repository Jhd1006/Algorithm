import sys
input = sys.stdin.readline

n, m = map(int, input().split())
p = [-1] * (n+1)

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

ans = []
for _ in range(m):
    x, a, b = map(int, input().split())
    if x == 0:
        union(a, b)
    elif x == 1:
        if find(a) == find(b):
            ans.append("YES")
        else:
            ans.append("NO")
print('\n'.join(ans))