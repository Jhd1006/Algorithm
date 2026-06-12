import sys
input = sys.stdin.readline

M, N = map(int, input().split())

L = list(map(int, input().split()))

start, end = 1, max(L)

while start <= end:
    mid = (start + end) // 2
    cnt = sum(l // mid for l in L if l >= mid)
    if cnt >= M:
        start = mid + 1
    elif cnt < M:
        end = mid - 1

print(end)
    