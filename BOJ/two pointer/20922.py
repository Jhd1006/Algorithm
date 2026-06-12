import sys
input = sys.stdin.readline

N, K = map(int, input().split())
a = list(map(int, input().split()))

en = 0
mx = 0
cnt = [0] * 100001
for st in range(N):
    while en < N and cnt[a[en]] < K:
        cnt[a[en]] += 1
        en += 1
    mx = max(mx, en -st)
    cnt[a[st]] -= 1

print(mx)

