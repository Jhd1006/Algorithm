# import sys 
# input = sys.stdin.readline

# def fun(num, cur, mod):
#     if cur == 0:
#         return 1
#     tmp = fun(num, cur//2, mod)
#     tmp = tmp * tmp % mod
#     if cur % 2 != 0:
#         tmp = tmp * num % mod   
#     return tmp 


# A, B, C = map(int, input().split())

# print(fun(A,B,C))

import sys
input = sys.stdin.readline

# def func(a, b, c):
#     if b == 0:
#         return 1
#     tmp = func(a, b//2, c)
#     tmp = tmp * tmp % c
#     if b % 2 != 0:
#         tmp = tmp * a % c
#     return tmp


# A, B, C = map(int, input().split())

# print(func(A, B, C))
sys.setrecursionlimit(10**6)
print(sys.getrecursionlimit())