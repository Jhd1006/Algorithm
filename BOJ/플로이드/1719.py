import sys
input = sys.stdin.readline

n, m = map(int, input().split())
inf = float('inf')
d = [[inf] * (n+1) for _ in range(n+1)]
nxt = [[0] * (n+1) for _ in range(n+1)]

for _ in range(m):
    u, v, time = map(int, input().split())
    d[u][v] = min(d[u][v], time)
    d[v][u] = min(d[v][u], time)
    nxt[u][v] = v
    nxt[v][u] = u

for i in range(1, n+1):
    d[i][i] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if d[i][j] > (d[i][k] + d[k][j]):
                d[i][j] = (d[i][k] + d[k][j])
                nxt[i][j] = nxt[i][k]

for i in range(1, n+1):
    for ds in nxt[i][1:]:
        if ds == 0:
            print('-', end = ' ')
        else:
            print(ds, end = ' ')
    print('')