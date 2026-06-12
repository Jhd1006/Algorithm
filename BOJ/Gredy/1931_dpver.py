import sys
input = sys.stdin.readline

N = int(input())
dp = [1] * N
time = []
for i in range(N):
    s, e = map(int, input().split())
    time.append((e, s))
time.sort()

for i in range(N):
    for j in range(i):
        if time[j][0] <= time[i][1]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))