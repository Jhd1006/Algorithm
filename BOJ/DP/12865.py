import sys
input = sys.stdin.readline

N, K = map(int, input().split())
bags = []
dp = [[0]*(K+1) for _ in range(N)]
for i in range(N):
    w, v = map(int, input().split())
    bags.append((w, v))

for i in range(1, K+1):
    w, v = bags[0]
    if w <= i:
        dp[0][i] = v

for i in range(1, N):
    w, v = bags[i]
    for j in range(1, K+1):
        if w <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N-1][K])




  
