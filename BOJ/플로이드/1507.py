import sys
input = sys.stdin.readline

N = int(input())
inf = float('inf')

d = [[0] for _ in range(N)]
for i in range(N): 
    d[i] = list(map(int, input().split()))
need = [[True] * (N) for _ in range(N)]

isPossible = True
for k in range(N):
    for i in range(N):
        for j in range(i, N):
            if k == i or k == j or i == j:
                continue
            if d[i][j] > d[i][k] + d[k][j]:
                isPossible = False
            elif d[i][j] == d[i][k] + d[k][j]:
                need[i][j] = False
                need[j][i] = False



if isPossible:
    for i in range(N):
        for j in range(N):
            if not need[i][j]:
                d[i][j] = 0
    ans = 0
    for i in range(N):
        ans += sum(d[i])
    print(ans//2)

else:
    print(-1)