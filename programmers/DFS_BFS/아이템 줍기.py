from collections import deque

# 왜 좌표를 2배로 늘리는가?
# 23   => 1 - 2 - 3 - 4 순으로 지나가야 하는데, 좌표를 2배로 늘리지 않으면 1-4로 가버릴 수 있음
# 14
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    board = [[0] * 102 for _ in range(102)]
    dist = [[-1] * 102 for _ in range(102)]

# 모든 직사각형 영역 1로 채워두고
    for x1, y1, x2, y2 in rectangle:
        x1 *= 2
        y1 *= 2
        x2 *= 2
        y2 *= 2
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                board[x][y] = 1

# 직사각형 내부는 0으로 파내기
    for x1, y1, x2, y2 in rectangle:
        x1 *= 2
        y1 *= 2
        x2 *= 2
        y2 *= 2               
        for x in range(x1 + 1, x2):
            for y in range(y1 + 1, y2):
                board[x][y] = 0
        
    
    characterX *= 2
    characterY *= 2
    itemX *= 2
    itemY *= 2
    
    q = deque([(characterX, characterY)])
    dist[characterX][characterY] = 0
    while q:
        x, y = q.popleft()
        if x == itemX and y == itemY:
            return dist[x][y] // 2
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if nx < 0 or nx >= 102 or ny < 0 or ny >= 102:
                continue
            if dist[nx][ny] == -1 and board[nx][ny] == 1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))
    return answer
