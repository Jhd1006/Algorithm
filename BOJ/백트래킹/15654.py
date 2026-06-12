import sys
input = sys.stdin.readline

N, M = map(int, input().split())
seq = list(map(int, input().split()))
seq.sort()
arr = [0] * M
isused = [False] * N

def func(cur):
    if cur == M:
        print(*arr)
        return
    for i in range(N):
       if isused[i]:
          continue
       isused[i] = True
       arr[cur] = seq[i]
       func(cur+1)
       isused[i] = False
func(0)

# 4 2
#  9 8 7 1

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