import sys
input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))


en = 0
mn = 100005
sum = 0

for st in range(N):
    while en < N and sum < S:
        sum += arr[en]
        en += 1
    if sum >= S:
        mn = min(mn, en - st)
    sum -= arr[st]
if mn == 100005:
    mn = 0

print(mn)



