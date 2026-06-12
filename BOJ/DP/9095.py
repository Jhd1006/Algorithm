import sys
input = sys.stdin.readline

T = int(input().strip())
result = []
for _ in range(T):
    dp = [0] * 11
    dp[1], dp[2], dp[3] = 1, 2, 4
    n = int(input().strip())
    for i in range(4, n+1):
        dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
    result.append(str(dp[n]))

print('\n'.join(result))

