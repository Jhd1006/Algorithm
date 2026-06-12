import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = [0]*M
isused = [False]*N

def func(cur):
    if cur == M:
        print(*arr)
        return
    start = 1
    if cur != 0:
        start = arr[cur-1] + 1
    for i in range(start, N+1):
        arr[cur] = i
        func(cur+1)
func(0)


# import sys
# input = sys.stdin.readline

# N, M = map(int, input().split())
# arr = [0] * M

# def func(cur, start): # 시작 지점을 인자로 받음
#     if cur == M:
#         print(*(arr)) # 리스트 언패킹(*)을 사용하면 더 간결함
#         return
    
#     for i in range(start, N + 1):
#         arr[cur] = i
#         func(cur + 1, i + 1) # 다음 단계에서는 현재 선택한 숫자보다 큰 값부터 탐색

# func(0, 1)