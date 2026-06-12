import sys
input = sys.stdin.readline

N = int(input())
dp = [0]*(N+2)
t = [0]*(N+2)
p = [0]*(N+2)
for i in range(1, N+1):
    t[i], p[i] = map(int, input().split())
for i in range(N, 0, -1):
    if (i + t[i]) <= N + 1:
        dp[i] = max(dp[i+1], dp[i+t[i]] + p[i])
    else:
        dp[i] = dp[i+1]
print(dp[1])


