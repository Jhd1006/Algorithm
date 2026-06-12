import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))

en = 0
cnt = 0
sum = 0

for st in range(N):
    while en < N and sum < M:
        sum += A[en]
        en += 1
    if sum == M:
        cnt += 1
    sum -= A[st]

print(cnt)
# 10 5
# 1 2 3 4 2 5 3 1 1 2

# 3