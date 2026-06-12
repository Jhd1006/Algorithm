import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
# 수, 종류, 연속, 쿠폰

dishcnt = [0] * (d+1)
arr = []
for _ in range(N):
    a = int(input())
    arr.append(a)


def func(arr, k):
    mx = 0
    cnt = 0
    arr = arr + arr[:k-1]

    dishcnt[c] += 1
    cnt += 1

    for i in range(k):
        if dishcnt[arr[i]] == 0:
            cnt += 1
        dishcnt[arr[i]] += 1
    mx = cnt
    for i in range(N-1):
        st = arr[i]
        en = arr[i+k]
        dishcnt[st] -= 1
        if dishcnt[st] == 0:
            cnt -= 1
        if dishcnt[en] == 0:
            cnt += 1
        dishcnt[en] += 1 
        mx = max(mx, cnt)
    return mx

print(func(arr, k))