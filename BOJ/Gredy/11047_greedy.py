import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = [int(input()) for _ in range(N)]

ans = 0
for i in range(N-1, -1, -1):
    ans += (K//A[i])
    K %= A[i]

print(ans)