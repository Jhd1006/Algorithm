import sys
input = sys.stdin.readline

N, M = map(int, input().split())

p = [-1] * (N+1)
edge = []

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

for _ in range(M):
    A, B, C = map(int, input().split())
    edge.append((C, A, B))
edge.sort()

sum = 0
cnt = 0
mx = 0
for cost, u, v in edge:
    if not union(u, v):
        continue
    cnt += 1
    sum += cost
    mx = cost
    if cnt == (N-1):
        break
print(sum - mx)