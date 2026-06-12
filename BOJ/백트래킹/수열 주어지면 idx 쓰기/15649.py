import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []

def func(start):
    if len(arr) == m:
        print(*arr)
        return
    for i in range(start, n+1):
        arr.append(i)
        func(i+ 1)
        arr.pop()

func(1)


