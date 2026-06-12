import sys
input = sys.stdin.readline

dx = [1, 0, -1, 0] # 남, 동, 북, 서
dy = [0, 1, 0, -1]

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
changed = [[0]* M for _ in range(N)]

def is_outofbound(x, y):
    return x < 0 or x >= N or y < 0 or y >= M

def change(x, y, dir):
    dir %= 4
    while True:
        x += dx[dir]
        y += dy[dir]
        if is_outofbound(x,y) or board[x][y] == 6:
            return
        if board[x][y] != 0:
            continue
        changed[x][y] = '#'

cctv = []
empty = 0
for i in range(N):
    for j in range(M):
        if board[i][j] != 0 and board[i][j] != 6:
            cctv.append((i, j))
        if board[i][j] == 0:
            empty += 1

for tmp in range(1 << (2*len(cctv))):
    for i in range (N):
        for j in range(M):
            changed[i][j] = board[i][j]
    brute = tmp
    for i in range(len(cctv)):
        dir = brute % 4
        brute //= 4
        x, y = cctv[i]
        if board[x][y] == 1:
            change(x, y, dir)
        elif board[x][y] == 2:
            change(x, y, dir)
            change(x, y, dir + 2)
        elif board[x][y] == 3:
            change(x, y, dir)
            change(x, y, dir + 1)
        elif board[x][y] == 4:
            change(x, y, dir)
            change(x, y, dir + 1)
            change(x, y, dir + 2)    
        else:
            change(x, y, dir)
            change(x, y, dir + 1)
            change(x, y, dir + 2)    
            change(x, y, dir + 3)
    cnt = 0
    for i in range(N):
        for j in range(M):
            if changed[i][j] == 0:
                cnt += 1
    empty = min(empty, cnt)
print(empty)

# import sys
# input = sys.stdin.readline
# # dir 0 : 남 / 1 : 동 / 2 : 북 / 3 : 서
# dx = [1, 0, -1, 0]
# dy = [0, 1, 0, -1]
# N, M = map(int, input().split())
# board = [list(map(int, input().split())) for _ in range(N)]
# sharp = [[0] * M for _ in range(N)]
# cctv = []
# empty = 0

# def check(a, b):
#     return a < 0 or a >= N or b < 0 or b >= M

# def change(x, y, dir):
#     dir %= 4
#     while True:
#         x += dx[dir]
#         y += dy[dir]
#         if check(x,y) or sharp[x][y] == 6:
#             return
#         if sharp[x][y] != 0:
#             continue
#         sharp[x][y] = 7

# for i in range(N):
#     for j in range(M):
#         if board[i][j] != 0 and board[i][j] != 6:
#             cctv.append((i, j))
#         if board[i][j] == 0:
#             empty += 1

# for tmp in range(1<<(2*len(cctv))):
#     for i in range(N):
#         for j in range(M):
#             sharp[i][j] = board[i][j]
#     brute = tmp
#     for i in range(len(cctv)):
#         dir = brute % 4
#         brute //= 4
#         x, y = cctv[i]
#         if board[x][y] == 1:
#             change(x, y, dir)
#         elif board[x][y] == 2:
#             change(x, y, dir)
#             change(x, y, dir+2)
#         elif board[x][y] == 3:
#             change(x, y, dir)
#             change(x, y, dir+1)
#         elif board[x][y] == 4:
#             change(x, y, dir)
#             change(x, y, dir+1)
#             change(x, y, dir+2)
#         else:
#             change(x, y, dir)
#             change(x, y, dir+1)
#             change(x, y, dir+2)
#             change(x, y, dir+3)

#     cnt = 0
#     for i in range(N):
#         for j in range(M):
#             if sharp[i][j] == 0:
#                 cnt += 1
#     empty = min(empty, cnt)

# print(empty)