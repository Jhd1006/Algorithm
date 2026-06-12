# import sys
# input = sys.stdin.readline
# n = int(input())
# wine = [int(input()) for _ in range(n)]
# dp = [0] * n

# dp[0] = wine[0]
# if n >= 2:
#     dp[1] = wine[0] + wine[1]
# if n >= 3:
#     dp[2] = max(dp[1], dp[0] + wine[2], wine[1] + wine[2])

# for i in range(3,n):
#     dp[i] = max(dp[i-1], dp[i-2] + wine[i], dp[i-3] + wine[i] + wine[i-1])

# print(dp[n-1])

#       o
# 1 2 3 4
#     x

import sys
input = sys.stdin.readline
n = int(input())
wine = [int(input()) for _ in range(n)]
dp = [[0] * 3 for _ in range(n)]

dp[0][1] = wine[0]
if n >= 2:
    dp[1][0] = dp[0][1]
    dp[1][1] = wine[1]
    dp[1][2] = dp[1][0] + wine[1]

for i in range(2, n):
    dp[i][0] = max(dp[i-1])
    dp[i][1] = dp[i-1][0] + wine[i]
    dp[i][2] = dp[i-1][1] + wine[i]

print(max(dp[n-1]))


