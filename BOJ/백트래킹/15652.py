import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [0] * M
def func(cur):
    if cur == M:
        print(*arr)
        return
    start = 1
    if cur != 0:
        start = arr[cur-1]
    for i in range (start, N+1):
        arr[cur] = i
        func(cur+1)
func(0)
# 1 1
# 1 2
# 1 3
# 1 4
# 2 2
# 2 3
# 2 4
# 3 3
# 3 4
# 4 4