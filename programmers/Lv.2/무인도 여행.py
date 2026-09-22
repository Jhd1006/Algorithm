from collections import deque

def solution(maps):
    answer = []
    h = len(maps)
    w = len(maps[0])   
    vis = [[False] *  w for _ in range(h)]
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    
    def bfs(i, j):
        q = deque([(i, j)])
        vis[i][j] = True
        cnt = 0
        while q:
            x, y = q.popleft()
            cnt += int(maps[x][y])
            for dir in range(4):
                nx = x + dx[dir]
                ny = y + dy[dir]
                if nx < 0 or nx >= h or ny < 0 or ny >= w:
                    continue
                if maps[nx][ny] == 'X' or vis[nx][ny]:
                    continue
                vis[nx][ny] = True
                q.append((nx, ny))
        return cnt
    
    for i in range(h):
        for j in range(w):
            if vis[i][j] or maps[i][j] =='X':
                continue
            answer.append(bfs(i, j))
            
    if answer:
        answer.sort()
    else:
        return [-1]

    return answer
