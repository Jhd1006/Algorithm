import sys
from collections import deque
input = sys.stdin.readline
dx= [1, 0, -1, 0]
dy = [0, 1, 0, -1]

T = int(input().strip())
result = []
for _ in range(T):
    q_s = deque()
    q_f = deque()
    w, h = map(int, input().split())
    board = [list(input().strip()) for _ in range (h)]
    dist_s = [[-1] * w for _ in range(h)]
    dist_f = [[-1] * w for _ in range(h)]
    
    for i in range(h):
        for j in range(w):
            if board[i][j] == '@':
                q_s = deque([(i, j)])
                dist_s[i][j] = 0
            elif board[i][j] == '*':
                q_f.append((i, j))
                dist_f[i][j] = 0
                
    isEscaped = False
    ans = 0
    while q_f:
        x, y = q_f.popleft()
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue
            if dist_f[nx][ny] != -1 or board[nx][ny] == '#':
                continue
            dist_f[nx][ny] = dist_f[x][y] + 1
            q_f.append((nx, ny))
    while q_s:
        x, y = q_s.popleft()
    
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                isEscaped = True
                ans = dist_s[x][y] + 1
                break
            if dist_s[nx][ny] != -1 or board[nx][ny] == '#':
                continue
            if dist_f[nx][ny] != -1 and dist_f[nx][ny] <= dist_s[x][y] + 1:
                continue
            dist_s[nx][ny] = dist_s[x][y] + 1
            q_s.append((nx, ny))
        if isEscaped :
            break
    result.append(str(ans) if isEscaped else "IMPOSSIBLE")
print('\n'.join(result))