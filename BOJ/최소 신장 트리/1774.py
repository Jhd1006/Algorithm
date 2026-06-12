import sys
input = sys.stdin.readline

N, M = map(int, input().split())
god = []
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

for _ in range(N):
    X, Y = map(int, input().split())
    god.append((X, Y))

edge = []
for i in range(N):
    for j in range(i + 1, N):
        d = (god[i][0] - god[j][0]) ** 2 + (god[i][1] - god[j][1]) ** 2
        dist = d ** 0.5
        edge.append((dist, i+1, j+1))
edge.sort()

con = 0
for _ in range(M):
    u, v = map(int, input().split())
    if union(u, v):
        con += 1

cnt = 0
ans = 0
for dist, u, v in edge:
    if not union(u, v):
        continue
    cnt += 1
    ans += dist
    if cnt == (N-1-con):
        break
print(f"{ans:.2f}")
