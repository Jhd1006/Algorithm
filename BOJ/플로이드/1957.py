import sys
input = sys.stdin.readline

V, E = map(int, input().split())
inf = float('inf')
d = [[inf] * (V+1) for _ in range(V+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    d[a][b] = c

for i in range(1, V+1):
    d[i][i] = 0

for k in range(1, V+1):
    for i in range(1, V+1):
        if d[i][k] == inf:
            continue
        for j in range(1, V+1):
            if d[i][j] > d[i][k] + d[k][j]:
                d[i][j] = d[i][k] + d[k][j]

dist = inf
for i in range(1, V+1):
    for j in range(i+1 ,V+1):
        if dist > d[i][j] + d[j][i]:
            dist = d[i][j] + d[j][i]

if dist != inf:
    print(dist)
else:
    print(-1)