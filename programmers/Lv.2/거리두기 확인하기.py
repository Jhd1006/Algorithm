from collections import deque

def solution(places):
    answer = []
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    def bfs(a, b, board):
        vis = [[False] * 5 for _ in range(5)]
        q = deque([(a, b, 0)])
        vis[a][b] = True

        while q:
            x, y, dist = q.popleft()
            if dist >= 2:
                continue
            for dir in range(4):
                nx = x + dx[dir]
                ny = y + dy[dir]
                if nx < 0 or nx >= 5 or ny < 0 or ny >= 5 or vis[nx][ny]:
                    continue
                if board[nx][ny] == 'X':
                    continue
                if board[nx][ny] == 'P':
                    return False
                vis[nx][ny] = True
                q.append((nx, ny, dist + 1))
        return True

    for board in places:
        ans = 1
        for i in range(5):
            for j in range(5):
                if board[i][j] == 'P':
                    if not bfs(i, j, board):
                        ans = 0
                        break
        answer.append(ans)
    
    return answer

============================= 반복문을 더 빨리 빠져나오록 => 함수 이용 ===============================
    def check(board):
            for i in range(5):
                for j in range(5):
                    if board[i][j] == 'P' and not bfs(i, j, board):
                        return 0  
            return 1
        
    for board in places:
        answer.append(check(board))
        
    return answer
