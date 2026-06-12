import sys
input =  sys.stdin.readline

N = int(input())
p = [-1] * (10**6+1)

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
    p[u] += p[v]
    p[v] = u
    return True

for _ in range(N):
    x = list(input().split())
    if x[0] == 'I':
        a, b = map(int, x[1:])
        union(a, b)

    elif x[0] == 'Q':
        c = find(int(x[1]))
        print(abs(p[c]))

        
