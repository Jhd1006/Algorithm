import sys
input = sys.stdin.readline

n, m = map(int, input().split())
seq = list(map(int, input().split()))
seq.sort()
idx = [0] * m

def func(cur):
    if cur == m:
        print(*[seq[i] for i in idx])
        return
    start = 0
    if cur != 0:
        start = idx[cur-1] + 1
    for i in range(start, n):
        idx[cur] = i
        func(cur + 1)

func(0)
