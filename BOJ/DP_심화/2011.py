import sys
input = sys.stdin.readline

pw = input().strip()

k = len(pw)
dp = [0] * (k+1)

pw = [0] + list(map(int, pw))

dp[0] = 1
dp[1] = 1

for i in range(2, k+1):
    if pw[i] != 0:
        dp[i] = (dp[i] + dp[i-1]) % 1000000
    x = pw[i-1] * 10 + pw[i] 
    if 10 <= x <= 26:
        dp[i] = (dp[i] + dp[i-2]) % 1000000

if pw[1] == 0:
    print(0)
else:
    print(dp[k])
