import sys
input = sys.stdin.readline

N = int(input().strip())
isused = [False] * N
isused2 = [False] * 2 * N
isused3 = [False] * 2 * N

cnt = 0
def chess(cur):
    global cnt
    if cur == N:
        cnt += 1
        return
    for i in range(N):
        if isused[i] or isused2[cur+i] or isused3[cur-i + N -1]:
            continue
        isused[i] = True
        isused2[cur + i] = True
        isused3[cur - i + N -1] = True
        chess(cur+1)
        isused[i] = False
        isused2[cur + i] = False
        isused3[cur - i + N -1] = False
chess(0)
print(cnt)

# import sys
# input = sys.stdin.readline

# N = int(input().strip())
# isused = [False] * N
# isused2 = [False] * 2 * N
# isused3 = [False] * 2 * N


# def chess(cur, cnt):
#     if cur == N:
#         return cnt + 1
#     for i in range(N):
#         if isused[i] or isused2[cur+i] or isused3[cur-i + N -1]:
#             continue
#         isused[i] = True
#         isused2[cur + i] = True
#         isused3[cur - i + N -1] = True
#         cnt = chess(cur+1, cnt)
#         isused[i] = False
#         isused2[cur + i] = False
#         isused3[cur - i + N -1] = False
#     return cnt

# ans = chess(0, 0)
# print(ans)

# x ㅁ ㅁ ㅁ 
# ㅁ ㅁ ㅁ ㅁ
# ㅁ ㅁ ㅁ ㅁ 
# ㅁ ㅁ ㅁ ㅁ  0-N-1이 최솟값, 인덱스 0 방지를 위해 + N-1
