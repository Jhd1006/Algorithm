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

W = []
for _ in range(N):
    w = int(input())
    W.append(w)

cost = [list(map(int, input().split())) for _ in range(N)]
edge = []

for i in range(N):
    for j in range(i, N):
        if i == j:
            edge.append((W[i], 0, i+1))
        else:
            edge.append((cost[i][j], i+1, j+1))
edge.sort()

cnt = 0
sum = 0
for cost, a, b in edge:
    if not union(a, b):
        continue
    cnt += 1
    sum += cost
    if cnt == N:
        break

print(sum)