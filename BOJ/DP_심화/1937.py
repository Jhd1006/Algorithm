import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
bamboo = [list(map(int, input().split())) for _ in range(n)]

d = [[-1] * n for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def panda(x, y):
    if d[x][y] != -1:
        return d[x][y]
    d[x][y] = 1
    for dir in range(4):
        nx = x + dx[dir]
        ny = y + dy[dir]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if bamboo[nx][ny] <= bamboo[x][y]:
            continue
        d[x][y] = max(d[x][y], panda(nx, ny) + 1)
    return d[x][y]

mx = 0
for i in range(n):
    for j in range(n):
        mx = max(mx, panda(i, j))

print(mx)