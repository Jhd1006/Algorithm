import sys
input = sys.stdin.readline
from bisect import bisect_left

K, N = map(int, input().split())
lines = []

for _ in range(K):
    l = int(input())
    lines.append(l)

start = 1
end = max(lines)
total = 0

def func(length):
    if length == 0:
        return True
    total = 0
    for l in lines:
        total += (l // length)
    return total >= N

while start < end:
    mid = (start + end + 1) // 2
    if func(mid):
        start = mid
    else:
        end = mid - 1



