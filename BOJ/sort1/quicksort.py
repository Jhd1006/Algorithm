# 6 -8 1 -7 3 8 7 12
# p          l r 
# 3 -8 1 -7 6 8 7 12 
# p         l r
# -7 -8 1 3 6 8 7 12 
# p   l r
# -8 -7 1 3 6 8 7 12

n = 8
arr1 = [4, -3, 15, 0, -9, 8, 2, -1]

arr2 = [10, -5, 6, -12, 7, 3, -2, 9]

arr3 = [-4, 11, -8, 5, 0, -6, 14, 2]

def quick_sort(arr, start, end):
    if start >= end:
        return
    pivot = arr[start]
    l = (start + 1)
    r = (end - 1)
    while True:
        while l <= r and arr[l] <= pivot:
            l += 1
        while l <= r and arr[r] >= pivot:
            r -= 1
        if l > r:
            break
        arr[l], arr[r] = arr[r], arr[l]
    arr[start], arr[r] = arr[r], arr[start]
    quick_sort(arr, start, r)
    quick_sort(arr, r+1, end)

quick_sort(arr1, 0, 8)
quick_sort(arr2, 0, 8)
quick_sort(arr3, 0, 8)

print(arr1)

print(arr2)

print(arr3)