import sys
input = sys.stdin.readline

N = int(input().strip())
board = [[' ']*(2*N-1) for _ in range(N)]

def fill(x, y):
    board[x][y] = '*'
    board[x+1][y-1] = '*'
    board[x+1][y+1] = '*'
    for i in range(5):
        board[x+2][y + i - 2] = '*'

def star(x, y, N):
    if N == 3:
        board[x][y] = '*'
        fill(x, y)
        return
    half = N // 2
    star(x, y, half)
    star(x + half, y - half, half)
    star(x + half, y + half, half)
star(0, N-1, N)
for i in range(N):
    print(''.join(map(str,board[i])))