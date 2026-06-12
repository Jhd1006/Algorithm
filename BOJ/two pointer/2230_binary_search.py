import sys
from bisect import bisect_left
input = sys.stdin.readline

N, M = map(int, input().split())
A = []
for _ in range(N):
    a = int(input())
    A.append(a)

A.sort()

mn = A[-1] - A[0]

for i in range(N):
    if A[i] + M <= A[-1]:
        idx = bisect_left(A, A[i] + M)
        mn = min(mn, A[idx]-A[i])

print(mn)
