import sys
input = sys.stdin.readline

n, m = map(int, input().split())
inf = float('inf')

d = [[inf] * (n+1) for _ in range(n+1)]
for _ in range(m):
    u, v, b = map(int, input().split())
    if b == 1:
        d[u][v] = 0
        d[v][u] = 0 
    elif b == 0:
        d[u][v] = 0
        d[v][u] = 1

for i in range(1, n+1):
    d[i][i] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])

k = int(input())
ans = []
for _ in range(k):
    s, e = map(int, input().split())
    ans.append(d[s][e])
print('\n'.join(map(str, ans)))
