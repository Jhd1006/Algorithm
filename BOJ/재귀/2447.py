# import sys
# input = sys.stdin.readline

# N = int(input().strip())
# board = [[' ']*N for _ in range(N)]

# def star(x, y, N):
#     if N ==1:
#         board[x][y] = '*'
#         return
#     n = N // 3
#     for i in range(3):
#         for j in range(3):
#             if i == 1 and j == 1:
#                 continue
#             star(x + n*i, y + n*j, n)
# star(0, 0, N)
# for i in range(N):
#     print(''.join(map(str,board[i])))

import sys
input = sys.stdin.readline

N = int(input().strip())
board = [[' ']*N for _ in range(N)]

def star(x, y, N):
    if N ==1:
        board[x][y] = '*'
        return
    n = N // 3
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            star(x + n*i, y + n*j, n)
star(0, 0, N)
for i in range(N):
    print(''.join(map(str,board[i])))