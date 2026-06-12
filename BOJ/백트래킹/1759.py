import sys
input = sys.stdin.readline

L, C = map(int, input().split())

S = list(input().split())
S.sort()

idx = [0] * L

def solve(cur, cnt):
    if cur == L:
        if cnt >= 1 and cnt <= L-2:
            print(''.join([S[i] for i in idx]))
        return
    start = 0 if cur == 0 else idx[cur-1] + 1
    for i in range(start, C):
        idx[cur] = i
        if S[i] in 'aeiou':
            solve(cur+1, cnt+1)
        else:
            solve(cur+1, cnt)
solve(0, 0)
# aeiou 한개 이상 자음 2개 이상
# 4 6
# a t c i s w
# => a c i s t w
# acis
# acit
# aciw
# acst
# acsw
# actw
# aist
# aisw
# aitw
# astw
# cist
# cisw
# citw
# istw