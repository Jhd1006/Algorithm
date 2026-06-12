import sys
input = sys.stdin.readline

N = int(input().strip())
dp = [0]*1000001
pre = [0]*1000001
dp[1] = 0

for i in range(2, N+1):
    dp[i] = dp[i-1] + 1
    pre[i] = i-1
    if i % 2 == 0 and dp[i//2] + 1 < dp[i]:
        dp[i] = dp[i//2] + 1
        pre[i] = i // 2
    if i % 3 == 0 and dp[i//3] + 1 < dp[i]:
        dp[i] =  dp[i//3] + 1
        pre[i] = i // 3

print(dp[N])

cur = N
result = []
while True:
    result.append(str(cur))
    if cur == 1:
        break
    cur = pre[cur]
print(' '.join(result))