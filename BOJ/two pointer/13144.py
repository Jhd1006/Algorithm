import sys
input = sys.stdin.readline

N = int(input())
arr= list(map(int, input().split()))

cnt = [False] * 100001

ans = 0
en = 0
for st in range(N):
    while en < N and not cnt[arr[en]]:
        cnt[arr[en]] = True
        en += 1
    ans += (en - st)
    cnt[arr[st]] = False
print(ans)
