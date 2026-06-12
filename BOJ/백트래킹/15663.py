import sys
input = sys.stdin.readline

n, m = map(int, input().split())
seq = list(map(int, input().split()))
seq.sort()
arr = [0]*m
isused = [False]*n

def func(cur):
    if cur == m:
        print(*arr)
        return
    tmp = None
    for i in range(0, n):
        if isused[i] or seq[i] == tmp:
            continue
        arr[cur] = seq[i]
        isused[i] = True
        tmp = seq[i]
        func(cur+1)
        isused[i] = False

func(0)
# 4 2 
# 9 7 9 1

# 1 7
# 1 9
# 7 1
# 7 9
# 9 1
# 9 7
# 9 9