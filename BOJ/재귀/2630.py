import sys
input = sys.stdin.readline

N = int(input().strip())
board = [list(map(int, input().split()))for _ in range(N)]
cnt = [0] * 2

def check(a, b, n):
    for i in range(a, a+n):
        for j in range(b, b+n):
            if board[i][j] != board[a][b]:
                return False
    return True

def recur(x, y, n):
    if check(x, y, n):
        cnt[board[x][y]] += 1
        return
    m = n // 2
    for i in range(2):
        for j in range(2):
            recur(x + i*m, y + j*m, m)

recur(0, 0, N)

print('\n'.join(map(str, cnt)))