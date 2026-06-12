import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
inf = float('inf')
d = [[inf] * (n+1) for _ in range(n+1)]
nxt = [[-1] * (n+1) for _ in range(n+1)]

for _ in range(1, m+1):
    a, b, c = map(int, input().split())
    d[a][b] = min(d[a][b], c)
    nxt[a][b] = b

for i in range(1, n+1):
    d[i][i] = 0

path = [[] for _ in range(n+1)]
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if d[i][k] + d[k][j] < d[i][j]:
                d[i][j] = d[i][k] + d[k][j]
                nxt[i][j] = nxt[i][k]

for i in range(1, n+1):
    for j in range(1, n+1):
        if d[i][j] == inf:
            print(0, end = ' ')
        else:
            print(d[i][j], end = ' ')
    print('')

for i in range(1, n+1):
    for j in range(1, n+1):
        if d[i][j] == 0 or d[i][j] == inf:
            print(0)
            continue
        st = i
        path = []
        while st != j:
            path.append(st)
            st = nxt[st][j]
        path.append(j)
        print(len(path), end = ' ')
        print(' '.join(map(str, path)))

