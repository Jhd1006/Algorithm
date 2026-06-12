import sys
from bisect import bisect_left
input = sys.stdin.readline

N, M = map(int, input().split())
A = []
for _ in range(N):
    a = int(input())
    A.append(a)

A.sort()
en = 0
mn = A[-1] - A[0]

for st in range(0, N):
  while en < N and (A[en] - A[st]) < M:
    en += 1
  if en == N:
     break
  mn = min(mn, A[en] - A[st])

print(mn)