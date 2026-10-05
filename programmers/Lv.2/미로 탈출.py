from collections import deque

def solution(maps):
    answer = 0
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    h = len(maps)
    w = len(maps[0])
    
    for i in range(h):
        for j in range(w):
            if maps[i][j] == 'S':
                start = (i, j)
            elif maps[i][j] == 'E':
                exit = (i, j)
            elif maps[i][j] == 'L':
                lever = (i, j)

    def bfs(start, end):
        dist = [[-1] * w for _ in range(h)]
        x, y = start
        q = deque([(x, y)])
        dist[x][y] = 0
        while q:
            x, y = q.popleft()
            if (x,  y) == end:
                return dist[x][y] 
            for dir in range(4):
                nx = x + dx[dir]
                ny = y + dy[dir]
                if nx < 0 or nx >= h or ny < 0 or ny >= w:
                    continue
                if maps[nx][ny] == 'X' or dist[nx][ny] != -1:
                    continue
                q.append((nx, ny))
                dist[nx][ny] = dist[x][y] + 1
        return -1

    result1 = bfs(start, lever)
    
    if result1 == -1:
        return -1

    result2 = bfs(lever, exit)
    
    if result2 == -1:
        return -1

    answer = result1 + result2
        
    return answer
