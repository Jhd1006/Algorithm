import sys
input = sys.stdin.readline

V, E = map(int, input().split())
edge = []
p = [-1] * (V+1)

def find(x):
    if p[x] < 0:
        return x
    p[x] = find(p[x])
    return p[x]

def is_diff_group(u, v):
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

for _ in range(E):
    A, B, C = map(int, input().split())
    edge.append((C, A, B))
edge.sort()

sum = 0
cnt = 0
for C, A, B in edge:
    if not is_diff_group(A, B):
        continue
    cnt += 1
    sum += C
    if cnt == (V-1):
        break
print(sum)

