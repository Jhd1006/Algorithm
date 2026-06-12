import sys
from bisect import bisect_left

A = [10, 40, 30, 60, 10, 50]

def compress(arr):
    unique_arr = list(set(arr))
    unique_arr.sort()
    for i in range(len(arr)):
        arr[i] = bisect_left(unique_arr, arr[i])
    
compress(A)

print(A)