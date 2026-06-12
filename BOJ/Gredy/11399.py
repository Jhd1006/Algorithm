import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int, input().split()))
P.sort()

wait = 0
sum =0
for i in range(N):
    wait += P[i]
    sum += wait
print(sum)