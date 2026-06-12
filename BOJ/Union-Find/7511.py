import sys
input = sys.stdin.readline

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

T = int(input())
ans = []
for test_case in range(1, T+1):
    n = int(input())
    k = int(input())
    p = [-1] * (n+1)
    for _ in range(k):
        a, b = map(int, input().split())
        union(a, b)
    m = int(input())

    ans.append(f"Scenario {test_case}:")

    for _ in range(m):
        u, v = map(int, input().split())
        if find(u) == find(v):
            ans.append("1")
        else:
            ans.append("0")
    ans.append('')
print('\n'.join(ans))

