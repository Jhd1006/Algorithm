import sys
input = sys.stdin.readline

dp = [0] * (100001)

N = int(input())

for i in range(1, N+1):
    dp[i] = i
    j = 1
    while (j*j) <= i:
        dp[i] = min(dp[i], dp[i-j*j]+1)
        j += 1

print(dp[N])

