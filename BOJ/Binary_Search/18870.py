import sys
input = sys.stdin.readline
from bisect import bisect_left

N = int(input())

X = list(map(int, input().split()))  

sorted_X = sorted(list(set(X)))
ans = []
for x in X:
    ans.append(bisect_left(sorted_X, x))
print(' '.join(map(str, ans)))
