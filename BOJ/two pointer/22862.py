import sys
input = sys.stdin.readline

N, K = map(int, input().split())
S = list(map(int, input().split()))

en = 0
cnt = 0
mx = 0

for st in range(0, N):
    while en < N and cnt <= K:
        cnt += (S[en] % 2)
        en += 1
    
    mx = max(mx, en - st - cnt)
    cnt -= (S[st] % 2)
print(mx)
