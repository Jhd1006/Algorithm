import sys
input = sys.stdin.readline

n, m = map(int, input().split())
seq = list(map(int, input().split()))
seq.sort()
idx = [0]*m

def func(cur):
    if cur == m:
        print(*[seq[i] for i in idx])
        return
    for i in range(n):
        idx[cur] = i
        func(cur+1)
func(0)

