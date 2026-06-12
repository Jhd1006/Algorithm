import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
p = [-1] * (N+1)

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

l = []
for _ in range(M):
    arr = list(map(int, input().split()))
    l.append(arr)
l.sort()

end = 0
for x, y in l:
    if y <= end:
        continue
    start = max(x, end)
    for i in range(start, y):
        union(i, i+1)
    end = y

ans = 0
for e in p[1:]:
    if e < 0:
        ans += 1

print(ans) 