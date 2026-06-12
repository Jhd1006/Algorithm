import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

T = int(input())

def acm(x, d, D):
    if d[x] != -1:
        return d[x]
    d[x]= 0
    for nxt in adj[x]:
        d[x] = max(d[x], acm(nxt, d, D))
    d[x] = d[x] + D[x]
    return d[x]

result = []

for _ in range(T):
    N, K = map(int, input().split())
    D = [0] + list(map(int, input().split()))
    d = [-1] * (N+1)
    adj = [[] for _ in range(N+1)]
    for _ in range(K):
        X, Y = map(int, input().split())
        adj[Y].append(X)
    W = int(input())
    result.append(acm(W, d, D))

print('\n'.join(map(str, result)))

