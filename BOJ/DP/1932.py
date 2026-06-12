import sys
input = sys.stdin.readline

dp = [[0]*502 for _ in range(502)]
n = int(input().strip())
tri = [list(map(int, input().split())) for _ in range(n)]
dp[0][0] = tri[0][0]
for i in range(n):
    for j in range(i+1):
        if j == 0:
            dp[i][j] = dp[i-1][j] + tri[i][j]
        elif j == i:
            dp[i][j] = dp[i-1][j-1] + tri[i][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + tri[i][j]

print(max(dp[n-1]))