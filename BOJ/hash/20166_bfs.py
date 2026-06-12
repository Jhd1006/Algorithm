import sys
input = sys.stdin.readline
from collections import deque

dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]
record = {}

def bfs(x, y):
    q = deque([(x, y, board[x][y])])
    if board[x][y] in record:
        record[board[x][y]] += 1
    else:
        record[board[x][y]] = 1
    while q:
        x, y, word = q.popleft()
        if len(word) > 5:
            continue
        for dir in range(8):
            nx = (x + dx[dir]) % N
            ny = (y + dy[dir]) % M
            next_word = word + board[nx][ny]
            if next_word in record:
                record[next_word] += 1
            else:
                record[next_word] = 1
            q.append((nx, ny, next_word))



N, M , K = map(int, input().split())

board = [input().strip() for _ in range(N)]

for i in range(N):
    for j in range(M):
        bfs(i, j)

ans = []

for _ in range(K):
    like = input().strip()
    if like not in record:
        ans.append('0')
    else: 
        ans.append(str(record[like]))
print('\n'.join(ans))
