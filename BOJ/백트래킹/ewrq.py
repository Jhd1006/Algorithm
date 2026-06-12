import sys
input = sys.stdin.readline

n, m = map(int, input().split())
seq = list(map(int, input().split()))
seq.sort()  # 중복 제거 및 오름차순 출력용
arr = [0] * m

def func(cur):
    if cur == m:
        print(*arr)
        return
    tmp = None
    for i in range(n):
        if seq[i] == tmp:
            continue
        arr[cur] = seq[i]  # ✅ 대입
        tmp = seq[i]       # ✅ 중복 방지
        func(cur + 1)

func(0)
