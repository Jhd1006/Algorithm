# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# seq = list(map(int, input().split()))
# seq.sort()
# idx = [0] * m
# isused = [False] * n

# def func(cur):
#     if cur == m:
#         print(*[seq[i] for i in idx])
#         return
#     tmp = None
#     start = 0 if cur == 0 else idx[cur-1]
#     for i in range(start, n):
#         if seq[i] == tmp:
#             continue
#         idx[cur] = i
#         tmp = seq[i]
#         func(cur+1)
# func(0)


import sys 
input = sys.stdin.readline

N, M = map(int, input().split())
seq = list(map(int, input().split()))
seq.sort()
idx = [0] * M
def nm(cur):
    if cur == M:
        print(*[seq[i] for i in idx])
        return
    start = 0 if cur == 0 else idx[cur-1] 
    tmp = None
    for i in range(start, N):
        if seq[i] == tmp:
            continue
        idx[cur] = i
        tmp = seq[i]
        nm(cur+1)
nm(0)