import sys
input = sys.stdin.readline

N = int(input().strip())

board =  [list(map(int, input().strip()))  for _ in range(N)]
ans = []

def check(x, y, n):
    for i in range(x, x+n):
        for j in range(y, y+n):
            if board[i][j] != board[x][y]:
                return False
    return True

def quadTree(x, y, n):
    if check(x, y, n):
        ans.append(board[x][y])
        return
    ans.append('(')
    half = n // 2
    quadTree(x, y, half)
    quadTree(x, y+half, half)
    quadTree(x+half, y, half)
    quadTree(x+half, y+half, half)
    ans.append(')')

quadTree(0, 0, N)
print(''.join(map(str, ans)))