import sys
input = sys.stdin.readline
from bisect import bisect_left

N = int(input())

feat = list(map(int, input().split()))

feat.sort()

print(bisect_left(feat, 1))


