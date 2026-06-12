import sys
input = sys.stdin.readline
arr = []
N = int(input())
for i in range(N):
    a = int(input())
    arr.append(a)

arr1 = arr[:]
arr1.sort()
for i in range(N):
    print(arr1[i])
print(f"arr1 : {arr1}")

tmp = [0]*N
arr2 = arr[:]
def merge(start, end):
    mid = (start + end) // 2
    lidx = start
    ridx = mid
    for i in range(start, end):
        if lidx == mid:
            tmp[i] = arr2[ridx]
            ridx += 1
        elif ridx == end:
            tmp[i] = arr2[lidx]
            lidx += 1
        elif arr[lidx] <= arr2[ridx]:
            tmp[i] = arr2[lidx]
            lidx += 1
        else:
            tmp[i] = arr2[ridx]
            ridx += 1
    arr2[start:end] = tmp[start:end]

def merge_sort(start, end):
    if end == (start + 1):
        return 1
    mid = (start + end) // 2
    merge_sort(start, mid)
    merge_sort(mid, end)
    merge(start, end)

merge_sort(0, N)
print(f"arr2 : {arr2}")
