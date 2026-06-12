import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
city = list(map(int, input().split()))
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

for c in city:
    union(0, c)

edge = []
for _ in range(M):
    u, v, w = map(int, input().split())
    edge.append((w, u, v))

edge.sort()

sum =0
cnt = 0
for w, u, v in edge:
    if not union(u, v):
        continue
    cnt += 1
    sum += w
    if cnt == (N-K):
        break
print(sum)
