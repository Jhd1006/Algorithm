import sys
input = sys.stdin.readline

k = int(input())
arr = list(map(int, input().split()))

def func(arr, k):
    n = len(arr)
    window = sum(arr[:k])
    mx = window
    for i in range(n-k):
        window = window - arr[i] + arr[i+k]
        mx = max(mx, window)
    return mx


print(func(arr, k))