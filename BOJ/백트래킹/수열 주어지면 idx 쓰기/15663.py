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
        if isused[i] or seq[i] == tmp:
            continue
        idx[cur] = i
        tmp = seq[i]
        isused[i] = True
        func(cur+1)
        isused[i] = False
func(0)

# def func(cur):
#     if cur == m:
#         print(*[seq[i] for i in idx])
#         return
#     start = idx[cur-1] + 1 if cur !=0 else 0
#     for i in range(start, n):
#         idx[cur] = i
#         func(cur+1)

# func(0)