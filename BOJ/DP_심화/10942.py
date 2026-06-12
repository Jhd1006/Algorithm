import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

M = int(input())

result = []
isPal = [[0] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
   isPal[i][i] = 1

for i in range(1, N):
   if nums[i-1] == nums[i]:
        isPal[i][i+1] = 1
   
for gap in range(2, N):
   for idx in range(1, N-gap+1):
      if nums[idx-1] == nums[idx+gap-1] and isPal[idx+1][idx+gap-1]:
        isPal[idx][idx+gap]= 1

for _ in range(M):
    S, E = map(int, input().split())
    result.append(isPal[S][E])


print('\n'.join(map(str, result)))