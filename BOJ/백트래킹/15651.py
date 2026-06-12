import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [0] * M
def func(cur):
    if cur == M:
        print(*arr)
        return
    for i in range(1,N+1):
        arr[cur] = i 
        func(cur+1) 
func(0)
# 1 1 1
# 1 1 2
# 1 1 3
# 1 2 1
# 1 2 2
# 1 2 3
# 1 3 1
# 1 3 2
# 1 3 3
# 2 1 1
# 2 1 2
# 2 1 3
# 2 2 1
# 2 2 2
# 2 2 3
# 2 3 1
# 2 3 2
# 2 3 3
# 3 1 1
# 3 1 2
# 3 1 3
# 3 2 1
# 3 2 2
# 3 2 3
# 3 3 1
# 3 3 2
# 3 3 3