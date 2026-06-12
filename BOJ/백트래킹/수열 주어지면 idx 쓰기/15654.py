import sys
input = sys.stdin.readline

n, m = map(int, input().split())
seq = list(map(int, input().split()))
idx = [0] * m
isused = [False] * n

def func(cur):
    if cur == m:
        print(*[seq[i] for i in idx])
        return
    for i in range(n):
        if isused[i]:
            continue
        idx[cur] = i
        isused[i] = True
        func(cur+1)
        isused[i] = False
func(0)



# 4 2
# 9 8 7 1

# 1 7
# 1 8
# 1 9
# 7 1
# 7 8
# 7 9
# 8 1
# 8 7
# 8 9
# 9 1
# 9 7
# 9 8