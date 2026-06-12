import sys
input = sys.stdin.readline
from itertools import permutations


N = int(input().strip())
A = list(map(int, input().split()))
op = list(map(int, input().split()))

mx = -float('inf')
mn = float('inf')

def dfs(idx, add, sub, mul, div, value):
    global mx, mn
    if idx == N:
        mx = max(mx, value)
        mn = min(mn, value)
        return
    if add:
        dfs(idx+1, add-1, sub, mul, div, value + A[idx])
    if sub:
        dfs(idx+1, add, sub-1, mul, div, value - A[idx])
    if mul:
        dfs(idx+1, add, sub, mul-1, div, value * A[idx])
    if div:
        if value > 0:
            dfs(idx+1, add, sub, mul, div-1, value // A[idx])
        else:
            dfs(idx+1, add, sub, mul, div-1, -(-value // A[idx]))
        
dfs(1, op[0], op[1], op[2], op[3], A[0])
print(mx)
print(mn)