import sys
input = sys.stdin.readline

n, k = map(int, input().split())

coin = []
inf = float('inf')
dp = [inf] * (k+1)

for _ in range(n):
    c = int(input())
    coin.append(c)

dp[0] = 0

for c in coin:
    for i in range(c, k+1):
        dp[i] = min(dp[i], dp[i-c] + 1)

print(-1 if dp[k] == inf else dp[k])
