import sys
input = sys.stdin.readline
dp = [0] * 1000005

T = int(input())
nums = [int(input())for _ in range(T)]

dp[1], dp[2], dp[3] = 1, 2, 4
ans = []

mx = max(nums)

for i in range(4, mx+1):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    dp[i] %= 1000000009

for num in nums:
    ans.append(str(dp[num]))
print('\n'.join(ans))
# 1 1 1
# 1 2
# 2 1
# 3