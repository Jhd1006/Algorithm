import sys
input = sys.stdin.readline

T = int(input())
result = []

for test_case in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    M = int(input())
    c = len(coins)
    d = [[0] * (M+1) for _ in range(N+1)]

    for i in range(N+1):
        d[i][0] = 1

    for i in range(1, N+1):
        for j in range(1, M+1):
            d[i][j] += d[i-1][j]
            if j >= coins[i-1]:
                d[i][j] += d[i][j-coins[i-1]]
    result.append(d[N][M])

print('\n'.join(map(str, result)))
