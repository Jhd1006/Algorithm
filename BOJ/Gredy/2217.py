import sys
input = sys.stdin.readline

N = int(input())
weight = [int(input()) for _ in range(N)]
weight.sort()

ans = 0
for i in range(0, N):
    ans = max(ans, weight[N-i-1]*(i+1))
print(ans)
