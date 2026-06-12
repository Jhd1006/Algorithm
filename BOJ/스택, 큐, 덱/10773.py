import sys
input = sys.stdin.readline

S = []
K = int(input())
for _ in range(K):
    n = int(input())
    if n == 0:
        S.pop()
    else:
        S.append(n)

print(sum(S))