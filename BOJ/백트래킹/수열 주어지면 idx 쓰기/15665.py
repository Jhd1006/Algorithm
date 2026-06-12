import sys
input = sys.stdin.readline

n, m = map(int, input().split())
seq = list(map(int, input().split()))
seq.sort()
idx = [0] * m
isused = [False] * n

def func(cur):
    if cur == m:
        print(*[seq[i] for i in idx])
        return
    tmp = None
    for i in range(n):
        if seq[i] == tmp:
            continue
        idx[cur] = i
        tmp = seq[i]
        func(cur+1)
func(0)
