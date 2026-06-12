import sys
input = sys.stdin.readline

n = int(input())
dp= [0]* n
nums = list(map(int, input().split()))

dp[0] = nums[0]
for i in range(1, n):
    dp[i] = max(nums[i], dp[i-1] + nums[i])

print(max(dp))
