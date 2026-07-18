from collections import deque
def solution(game_board, table):
    answer = 0
    l = len(game_board[0])
    dx = [-1, 0, 1, 0]
    dy = [0,-1, 0, 1]
    vis_g = [[False] * 52 for _ in range(52)]
    vis_t = [[False] * 52 for _ in range(52)]
    pieces = []
    blanks = []
    def bfs(x, y, vis, k, board):
        piece = []
        q = deque([(x, y)])
        vis[x][y] = True
        piece.append((x, y))
        while q:
            x, y = q.popleft()
            for dir in range(4):
                nx = x + dx[dir]
                ny = y + dy[dir]
                if nx < 0 or nx >= l or ny < 0 or ny >= l:
                    continue
                if board[nx][ny] != k or vis[nx][ny]:
                    continue
                vis[nx][ny] = True
                q.append((nx, ny))
                piece.append((nx, ny))
        return piece
    
    def normalize(piece):
        min_x = min(x for x, y in piece)
        min_y = min(y for x, y in piece)
        return sorted((x - min_x, y - min_y) for x, y in piece)
    
    def rotate(piece):
        return normalize([(y, -x) for x, y in piece])
    
    for i in range(l):
        for j in range(l):
            if vis_t[i][j] or table[i][j] != 1:
                continue
            piece = bfs(i, j, vis_t, 1, table)
            pieces.append(normalize(piece))
    for i in range(l):
        for j in range(l):
            if vis_g[i][j] or game_board[i][j] != 0:
                continue
            blank = bfs(i, j, vis_g, 0, game_board)
            blanks.append(normalize(blank))
            
    used = [False] * len(pieces)
    for blank in blanks:
        for idx, piece in enumerate(pieces):
            if used[idx]:
                continue
            tmp = piece
            for _ in range(4):
                if tmp == blank:
                    answer += len(blank)
                    used[idx] = True
                    break
                tmp = rotate(tmp)
            if used[idx]:
                break
    if answer == -1:
        answer = 0
    return answer
