#고정석 사이의 구간에서의 경우의 수들끼리 곱해줌

import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
V = [int(input()) for _ in range(M)]

V = [0] + V + [N+1]
dp = [0] * (N+1)

dp[0], dp[1] = 1, 1

for i in range(2, N+1):
    dp[i] = dp[i-2] + dp[i-1]

ans = 1
for i in range(1, len(V)):
    ans *= (dp[V[i] - V[i-1] - 1])
print(ans)


# dp = [0]*(N+1)
# dp[0] = 1
# dp[1] = 1
# result = []
# for i in range(2, N+1):
#     if i in V or i - 1 in V:
#         dp[i] = dp[i-1]
#         continue
#     dp[i] = dp[i-2] + dp[i-1]
# print(dp[N])


