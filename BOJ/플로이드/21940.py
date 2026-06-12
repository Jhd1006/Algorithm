import sys
input = sys.stdin.readline

N, M = map(int, input().split())
inf = float('inf')
d = [[inf] * (N+1) for _ in range(N+1)]

for _ in range(M):
    a, b, t = map(int, input().split())
    d[a][b] = min(d[a][b], t)

K = int(input())
C = list(map(int, input().split()))

for i in range(1, N+1):
    d[i][i] = 0

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])


dists = []
for i in range(1, N+1):
    dist = 0
    for c in C:
        dist = max(dist, d[i][c] + d[c][i])
    dists.append(dist)
    
mn = min(dists)
ans = []
for idx, val in enumerate(dists):
    if val == mn:
        ans.append(idx+1)
print(' '.join(map(str, ans)))