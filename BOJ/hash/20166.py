import sys
input = sys.stdin.readline

dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]
record = {}

def dfs(x, y, word):
    if len(word) > 5:
        return
    if word in record:
        record[word] += 1
    else:
        record[word] = 1
    for dir in range(8):
        nx = (x + dx[dir]) % N
        ny = (y + dy[dir]) % M
        dfs (nx, ny, word + board[nx][ny])

N, M , K = map(int, input().split())

board = [input().strip() for _ in range(N)]

for i in range(N):
    for j in range(M):
        dfs(i, j, board[i][j])

ans = []

for _ in range(K):
    like = input().strip()
    if like not in record:
        ans.append('0')
    else: 
        ans.append(str(record[like]))
print('\n'.join(ans))
