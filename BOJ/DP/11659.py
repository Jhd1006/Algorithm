import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
dp=[0]*(N+1)
for i in range(1,N+1):
    dp[i] = dp[i-1] + nums[i-1]
result = []
for _ in range(M):
    i, j = map(int, input().split())
    result.append(str(dp[j]-dp[i-1]))

print('\n'.join(result))

