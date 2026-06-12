import sys
input = sys.stdin.readline
from bisect import bisect_left
from bisect import bisect_right

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
ans = []

A.sort()
def binarysearch(target):

    # idx = bisect_left(A, target)
    # if idx < N and A[idx] == target:
    #     return 1
    # return 0

    idx = bisect_right(A, target)
    if idx >= 0 and A[idx-1] == target:
        return 1
    return 0

    
    # start = 0
    # end = N -1
    # while (start <= end):
    #     mid = (start + end) // 2
    #     if (A[mid] < target):
    #         start = mid + 1
    #     elif A[mid] > target:
    #         end = mid -1
    #     else:
    #         return 1
    # return 0

for b in B:
    ans.append(binarysearch(b))

print('\n'.join(map(str, ans)))

