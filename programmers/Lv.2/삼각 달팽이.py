def solution(n):
    answer = []
    arr = [[0] * x for x in range(1, n + 1)]
    dx = [1, 0, -1]
    dy = [0, 1, -1]
    dir = 0
    tot = (n * (n + 1)) // 2
    x, y, = 0, 0
    
    for i in range(1, tot + 1):
        arr[x][y] = i
        nx = x + dx[dir]
        ny = y + dy[dir]
        if nx < 0 or nx >= n or ny < 0 or ny > nx or arr[nx][ny] != 0:
            dir = (dir + 1) % 3
            nx = x + dx[dir]
            ny = y + dy[dir]
        x, y = nx, ny

        
    return [r for row in arr for r in row]
