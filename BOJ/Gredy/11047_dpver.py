import sys
input = sys.stdin.readline

N, K = map(int, input().split())

A = [int(input()) for _ in range(N)]

dp = [float('inf')] * (K+1)
dp[0] = 0


for coin in A:
    for i in range(coin, K+1):
        dp[i] = min(dp[i], dp[i-coin]+1)

print(dp[K])
