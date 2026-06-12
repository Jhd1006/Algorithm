import sys
input = sys.stdin.readline

N = int(input())

dp = [0] * (N+1)

dp[2] = 3

for i in range(4, N+1, 2):
    dp[i] = dp[i-2] * 3
    dp[i] += dp[i-4] * 2

print(dp)
