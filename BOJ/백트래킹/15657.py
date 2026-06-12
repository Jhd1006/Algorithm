import sys
input = sys.stdin.readline

n, m = map(int, input().split())
seq = list(map(int, input().split()))
seq.sort()
arr = [0] * m

def func(cur):
    if cur == m:
        print(*arr)
        return
    
    if cur == 0:
        start = 0
    else:
        start = seq.index(arr[cur-1])
    for i in range(start, n):
        arr[cur] = seq[i]
        func(cur+1)

func(0)

# 4 2
# 9871

# 1 1
# 1 7
# 1 8
# 1 9
# 7 7
# 7 8
# 7 9
# 8 8
# 8 9
# 9 9