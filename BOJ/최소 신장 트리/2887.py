import sys
input = sys.stdin.readline

N = int(input())
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

planet = []
for i in range(N):
    x, y, z = map(int, input().split())
    planet.append((x, y, z, i+1))

edge = []
for dir in range(3):
    planet.sort(key = lambda x:x[dir])
    for i in range(N-1):
        cost = abs(planet[i][dir] - planet[i+1][dir])
        edge.append((cost, planet[i][3], planet[i+1][3]))
cnt = 0
ans = 0
edge.sort()

for cost, u, v in edge:
    if not union(u, v):
        continue
    cnt += 1
    ans += cost
    if cnt == (N-1):
        break
print(ans)

