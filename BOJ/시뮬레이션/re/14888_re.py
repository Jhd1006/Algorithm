# import sys
# input = sys.stdin.readline

# mx = -float('inf')
# mn = float('inf')

# N = int(input())
# A = list(map(int, input().split()))
# op = list(map(int, input().split()))


# def func(idx, add, sub, mul, div, val):
#     global mn, mx
#     if idx == N:
#         mx = max(val, mx)
#         mn = min(val, mn)
#         return
#     if add:
#         func(idx+1, add-1, sub, mul, div, val+A[idx])
#     if sub:
#         func(idx+1, add, sub-1, mul, div, val-A[idx])
#     if mul:
#         func(idx+1, add, sub, mul-1, div, val*A[idx])
#     if div:
#         if val > 0:
#             func(idx+1, add, sub, mul, div-1, val // A[idx])
#         else:
#             func(idx+1, add, sub, mul, div-1, -(-val // A[idx]))

# func(1, op[0], op[1], op[2], op[3], A[0])
# print(mx)
# print(mn)
import sys
input = sys.stdin.readline

mx = -float('inf')
mn = float('inf')

N = int(input())
A = list(map(int, input().split()))
op = list(map(int, input().split()))


def func(idx, add, sub, mul, div, val):
    global mn, mx
    if idx == N:
        mx = max(val, mx)
        mn = min(val, mn)
        return
    if add:
        func(idx+1, add-1, sub, mul, div, val+A[idx])
    if sub:
        func(idx+1, add, sub-1, mul, div, val-A[idx])
    if mul:
        func(idx+1, add, sub, mul-1, div, val*A[idx])
    if div:
        if val > 0:
            func(idx+1, add, sub, mul, div-1, val // A[idx])
        else:
            func(idx+1, add, sub, mul, div-1, -(-val // A[idx]))

func(1, op[0], op[1], op[2], op[3], A[0])
print(mx)
print(mn)