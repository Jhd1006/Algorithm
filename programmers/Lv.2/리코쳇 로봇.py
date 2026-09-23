from collections import deque

def solution(board):
    answer = 0
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    h = len(board)
    w = len(board[0])
    
    def ricochet(i, j):
        vis = [[False] * w for _ in range(h)]
        q = deque([(i, j, 0)])
        while q:
            x, y, cnt = q.popleft()
            if board[x][y] == 'G':
                return cnt
            for dir in range(4):
                nx, ny = x, y
                while True:
                    nx += dx[dir]
                    ny += dy[dir]
                    if nx < 0 or nx >= h or ny < 0 or ny >= w or board[nx][ny] == 'D':
                        nx -= dx[dir]
                        ny -= dy[dir]
                        break
                if vis[nx][ny]:
                    continue
                vis[nx][ny] = True
                q.append((nx, ny, cnt + 1))
        return -1
                    
    for i in range(h):
        for j in range(w):
            if board[i][j] == 'R':
                answer = ricochet(i, j)
            
    return answer
