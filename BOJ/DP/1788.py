import sys
input = sys.stdin.readline
n = int(input())
a = abs(n)
dp = [0] * (a+2)
dp[1] = 1
for i in range(2, a+1):
    dp[i] = dp[i-2] + dp[i-1]
    dp[i] %= 1000000000
if n < 0 and a % 2 == 0:
    print(-1)
elif n == 0:
    print(0)
else:
    print(1)
print(dp[a])

