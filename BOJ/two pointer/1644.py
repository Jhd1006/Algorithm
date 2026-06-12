import sys
input = sys.stdin.readline

N = int(input())
prime = []
isprime = [True] * (N+1)
isprime[0] = isprime[1] = False

for i in range(2, int(N**0.5) + 1):
    if isprime[i]:
        for j in range(i*i, N+1, i):
            isprime[j] = False
for i in range(len(isprime)):
    if isprime[i]:
        prime.append(i)

cnt = 0
en = 0
tot = 0

for st in range(len(prime)):
    while en < len(prime) and tot < N:
        tot += prime[en]
        en += 1
    if tot == N:
        cnt += 1
    tot -= prime[st]

print(cnt)

# 3 : 3 (한 가지)
# 41 : 2+3+5+7+11+13 = 11+13+17 = 41 (세 가지)
# 53 : 5+7+11+13+17 = 53 (두 가지)
# 출력
# 첫째 줄에 자연수 N을 연속된 소수의 합으로 나타낼 수 있는 경우의 수를 출력한다.