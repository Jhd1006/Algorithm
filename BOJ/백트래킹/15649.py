import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [0] * m
isused = [False] * n


def func(k):
    if (k == m):
        print(' '.join(map(str, arr)))
        return
    for i in range(n):
        if not isused[i]:
            arr[k] = i + 1
            isused[i] = True
            func(k+1)
            isused[i] = False

func(0)