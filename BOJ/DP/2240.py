import sys
input = sys.stdin.readline

T, W = map(int, input().split())
plum = [0] + [int(input()) for _ in range(T)]
dp = [[0]*(W+1) for _ in range(T+1)]

for i in range(1, T+1):
    dp[i][0] = dp[i-1][0]
    if plum[i] == 1:
        dp[i][0] += 1

for i in range(1, T+1):
    for j in range(1, W+1):
        dp[i][j] = max(dp[i-1][j-1] , dp[i-1][j]) 
        if (j % 2 + 1) == plum[i]:
            dp[i][j] += 1
print(max(dp[T]))

