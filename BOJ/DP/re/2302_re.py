import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
v = [int(input()) for _ in range(M)]
v = [0] + v + [N+1]
dp = [0] * (N+1)

dp[0], dp[1] = 1, 1
for i in range(2, N+1):
    dp[i] = dp[i-2] + dp[i-1]
ans = 1
for i in range(1, len(v)):
    ans *= (dp[v[i] -v[i-1] -1])
print(ans)