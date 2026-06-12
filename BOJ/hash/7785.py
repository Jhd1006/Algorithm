import sys
input = sys.stdin.readline

n = int(input())

S = set()
for _ in range(n):
    a, b = map(str, input().split())
    if b == "enter":
        S.add(a)
    elif b == "leave":
        S.discard(a)
L = sorted(S, reverse=True)
for l in L:
    print(l)
