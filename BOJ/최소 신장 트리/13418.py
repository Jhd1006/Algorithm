import sys
input = sys.stdin.readline

N, M = map(int, input().split())
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

edge = []
for _ in range(M+1):
    A, B, C = map(int, input().split())
    edge.append((C, A, B))
edge.sort()

up = 0
cnt = 0
for cost, u, v in edge:
    if not union(u, v):
        continue
    cnt += 1
    up += (1-cost)
    if cnt == (N):
        break
mx = up ** 2

p = [-1] * (N+1)
up = 0
cnt = 0
edge.sort(reverse = True)
for cost, u, v in edge:
    if not union(u, v):
        continue
    cnt += 1
    up += (1-cost)
    if cnt == (N):
        break
mn = up ** 2

print(mx -mn)
