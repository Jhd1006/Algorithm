import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
A = list(map(int, input().split()))

dp = [1]*N
pre = [-1]*N
for i in range(N):
    for j in range(i):
        if A[i] > A[j] and dp[j] + 1 > dp[i]:
            dp[i] = dp[j]+1
            pre[i] = j
mx = max(dp)
idx = dp.index(mx)
print(mx)

idxs = deque()
while idx != -1:
    idxs.append(idx)
    idx = pre[idx]
while idxs:
    i = idxs.pop()
    print(A[i], end=' ')