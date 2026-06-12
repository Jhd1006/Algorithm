import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
p = [-1] * (n)

def find(x):
    if p[x] < 0:
        return x
    p[x] = find(p[x])
    return p[x]
    
def union(u, v):
    u = find(u)
    v = find(v)
    if v == u:
        return False
    if p[v] < p[u]:
        u, v = v, u
    if p[u] == p[v]:
        p[u] -= 1
    p[v] = u
    return True

num = 0
for i in range(m):
    u, v = map(int, input().split())
    if not union(u, v) and num == 0:
        num = (i+1)
print(num)