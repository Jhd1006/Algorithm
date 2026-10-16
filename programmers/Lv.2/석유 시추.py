from collections import deque

def solution(land):
    answer = 0
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    w, h = len(land[0]), len(land)
    vis = [[False] * w for _ in range(h)]
    take = [0] * w
           
    def oil(i, j):        
        q = deque([(i, j)])
        vis[i][j] = True
        cnt = 1
        col = set([j])
        while q:
            x, y = q.popleft()
            for dir in range(4):
                nx = x + dx[dir]
                ny = y + dy[dir]
                if nx < 0 or nx >= h or ny < 0 or ny >= w:
                    continue
                if land[nx][ny] != 1 or vis[nx][ny]:
                    continue
                vis[nx][ny] = True
                cnt += 1
                q.append((nx, ny))
                col.add(ny)
        for s in col:
            take[s] += cnt
        return
    
    for i in range(h):
        for j in range(w):
            if land[i][j] == 1 and not vis[i][j]:
                oil(i, j)

    answer = max(take)   
    return answer
