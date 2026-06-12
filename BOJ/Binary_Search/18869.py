import sys
input = sys.stdin.readline
from bisect import bisect_left

M, N = map(int, input().split())

A = [[0] * N for _ in range(M)]
for i in range (M):
    A[i] = list(map(int, input().split()))


def compress(arr):
    unique_arr = list(set(arr))
    unique_arr.sort()
    for i in range(N):
        arr[i] = bisect_left(unique_arr, arr[i])

for i in range(M):
    compress(A[i])

cnt = 0

for i in range(M-1):
    for j in range(i+1, M):
        if A[i] == A[j]:
            cnt += 1
print(cnt)