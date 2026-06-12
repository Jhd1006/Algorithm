import sys
input = sys.stdin.readline

T = int(input())
dp = [0] * 101
dp[0], dp[1], dp[2] = 1, 1, 1
result = []
for _ in range(T):
    N = int(input())
    for i in range(3, N):
        dp[i] = dp[i-3] + dp[i-2]
    result.append(str(dp[N-1]))
print('\n'.join(result))
