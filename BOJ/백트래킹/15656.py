import sys
input = sys.stdin.readline

n, m = map(int, input().split())
seq = list(map(int, input().split()))
arr = [0]*m
seq.sort()
isused = [False] * n

def func(cur):
    if cur == m:
        print(*arr)
        return
    start = 0
    for i in range(start, n):
        arr[cur] = seq[i]
        isused[i] = True
        func(cur+1)
        isused[i] = False

func(0)
