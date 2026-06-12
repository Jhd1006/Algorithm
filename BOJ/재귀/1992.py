import sys
input = sys.stdin.readline

N = int(input().strip())
board= [list(map(int, input().strip())) for _ in range(N)]
ans = []
def check(x, y, n):
    for i in range(x, x+n):
        for j in range(y, y+n):
            if board[i][j] != board[x][y]:
                return False
    return True

def recur(x, y, n):
    if check(x, y, n):
        ans.append(board[x][y])
        return
    ans.append('(')
    half = n // 2
    dx = [0, 0, half, half]
    dy = [0, half, 0, half]
    for dir in range(4):
        recur(x+dx[dir], y+dy[dir], half)
    ans.append(')')

recur(0, 0, N)
print(''.join(map(str, ans)))
