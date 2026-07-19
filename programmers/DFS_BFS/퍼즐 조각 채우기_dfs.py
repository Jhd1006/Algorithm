from collections import deque
def solution(game_board, table):
    answer = 0
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    l = len(table[0])
    vis_g = [[False] * 52 for _ in range(52)]
    vis_t = [[False] * 52 for _ in range(52)]
    cell = []
    blanks = []
    pieces = []
    
    def find(x, y, vis, board, k):
        cell.append((x, y))
        vis[x][y] = True
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if nx < 0 or nx >= l or ny < 0 or ny >= l:
                continue
            if board[nx][ny] != k or vis[nx][ny]:
                continue
            find(nx, ny, vis, board, k)
        return cell
    
    def normalize(cell):
        min_x = min(x for x, y in cell)
        min_y = min(y for x, y in cell)
        return sorted((x - min_x, y - min_y) for x, y in cell)
    
    def rotate(piece):
        return normalize([(y, -x) for x, y in piece])
    
    for i in range(l):
        for j in range(l):
            if vis_g[i][j] or game_board[i][j] == 1:
                continue
            cell = []
            blank = find(i, j, vis_g, game_board, 0)
            blanks.append(normalize(blank))
            
    for i in range(l):
        for j in range(l):
            if vis_t[i][j] or table[i][j] == 0:
                continue
            cell = []
            piece = find(i, j, vis_t, table, 1)
            pieces.append(normalize(piece))

    used = [False] * len(pieces)
    
    for blank in blanks:
        for idx, piece in enumerate(pieces):
            if used[idx]:
                continue
            tmp = piece
            for _ in range(4):
                if tmp == blank:
                    answer += len(tmp)
                    used[idx] = True
                    break
                tmp = rotate(tmp)
            if used[idx]:
                break   
                
    if answer == -1:
        answer = 0
        
    return answer
