import sys
input = sys.stdin.readline

N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]
p = [-1] * (N+1)

def find(x):
    if p[x] < 0:
        return x
    p[x] = find(p[x])
    return p[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return False
    if p[b] < p[a]:
        a, b = b, a
    if p[a] == p[b]:
        p[a] -= 1
    p[b] = a
    return True

edge = []
for i in range(N):
    for j in range(i+1, N):
        edge.append((cost[i][j], i+1, j+1))
edge.sort()

cnt = 0
sum = 0
for cost, u, v in edge:
    if not union(u, v):
        continue
    union(u, v)
    cnt += 1
    sum += cost

print(sum)


