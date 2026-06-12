import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
dp = [1] * N
pre = [-1] * N

for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            if dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1 
                pre[i] = j
mx = max(dp)
print(mx)

ans=[]
idx = dp.index(mx)
while idx != -1:
    ans.append(A[idx])
    idx = pre[idx]
ans.reverse()
print(' '.join(map(str, ans)))
    
