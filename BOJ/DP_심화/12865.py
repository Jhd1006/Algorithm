import sys
input = sys.stdin.readline

N, K = map(int, input().split())

dp = [[0] * (K+1) for _ in range(N+1)]
w = []
v = []

for _ in range(N):
    W, V = map(int, input().split())
    w.append(W)
    v.append(V)

for i in range(1, N+1):
    for j in range(1, K+1):
        if w[i-1] <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i-1]] + v[i-1])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N][K])