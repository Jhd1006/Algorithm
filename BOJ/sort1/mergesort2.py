
n = 10
tmp = [0] * n #merge 함수에서 리스트 2개를 합친 결과를 임시로 저장하고 있을 변수
arr = [15, 25, 22, 357, 16, 23, -53, 12, 46, 3]


def merge(start, end):
    mid = (start + end) // 2   #arr[start:mid], arr[mid:end]는 정렬되어있음 (이 둘을 합쳐야 함)
    lidx = start
    ridx = mid
    for i in range(start, end):
        if ridx == end:
            tmp[i] = arr[lidx]
            lidx += 1
        elif lidx == mid:
            tmp[i] = arr[ridx]
            ridx += 1
        elif arr[lidx] <= arr[ridx]:
            tmp[i] = arr[lidx]
            lidx += 1
        else:
            tmp[i] = arr[ridx]
            ridx += 1
    arr[start:end] = tmp[start:end]

def merge_sort(start, end):
    if end == start + 1:
        return 1
    mid = (start + end) // 2 
    merge_sort(start, mid)
    merge_sort(mid, end)
    merge(start, end)


merge_sort(0, n)
print(arr) #-53 3 12 15 16 22 23 25 46 357


