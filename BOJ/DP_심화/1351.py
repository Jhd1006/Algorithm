import sys
input = sys.stdin.readline

N, P, Q = map(int, input().split())

# A[i] = A[i/p] + A[i/q]

A = {}

def func(n):
    if n == 0:
        return 1
    if n in A:
        return A[n]
    A[n] = func(n//P) + func(n//Q)
    return A[n] 

print(func(N))

