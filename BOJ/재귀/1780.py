# import sys
# input = sys.stdin.readline

# N = int(input().strip())

# board = [list(map(int, input().split())) for _ in range(N)]
# cnt = [0, 0, 0]

# def check(x, y, n):
#     for i in range(x, x + n):
#         for j in range(y, y + n):
#             if board[i][j] != board[x][y]:
#                 return False
#     return True

# def func(x, y, n):
#     if check(x, y, n):
#         cnt[board[x][y]+1] += 1
#         return
#     m = n // 3
#     for i in range(3):
#         for j in range(3):
#             func(x + i * m, y + j * m, m)
# func(0, 0, N)
# print('\n'.join(map(str, cnt)))

import sys
input = sys.stdin.readline
N = int(input().strip())
board = [list(map(int, input().split())) for _ in range(N)]
cnt = [0] * 3
def check(x, y, n):
    for i in range (x, x+n):
        for j in range (y, y+n):
            if board[i][j] != board[x][y]:
                return False
    return True

def func(x, y, n):
    if check(x, y, n):
        cnt[board[x][y] + 1] += 1
        return
    m = n // 3
    for i in range (3):
        for j in range (3):
            func(x + i*m, y + j*m, m)
func(0, 0, N)
print('\n'.join(map(str, cnt)))

