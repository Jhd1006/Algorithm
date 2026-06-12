import sys
input = sys.stdin.readline

zero = [0] * 42
one = [0] * 42

T = int(input().strip())
zero[0], zero[1] = 1, 0
one[0], one[1] = 0, 1

ans = []
for _ in range(T):
    N = int(input().strip())
    for i in range(2, N+1):
        zero[i] = zero[i-1] + zero[i-2]
        one[i] = one[i-1] + one[i-2]
    ans.append((zero[N], one[N]))
for z, o in ans:
    print(z, o)


