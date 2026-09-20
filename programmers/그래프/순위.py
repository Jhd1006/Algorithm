from collections import deque

def solution(n, results):
    answer = 0
    win = [[] for _ in range(n+1)]
    lose = [[] for _ in range(n+1)]
    
    for u, v in results:
        win[u].append(v)
        lose[v].append(u)
        
    def bfs(start, adj):
        cnt = 0
        vis = [-1] * (n+1)
        q = deque([start])
        vis[start] = 0
        while q:
            cur = q.popleft()
            for nxt in adj[cur]:
                if vis[nxt] != -1:
                    continue
                vis[nxt] = 0
                cnt += 1
                q.append(nxt)
        return cnt
    
    for i in range(1, n+1):
        if bfs(i, win) + bfs(i, lose) == n-1:
            answer += 1   
            
    return answer

## 플로이드 - 워셜 사용 ##

def solution(n, results):
    answer = 0
    win = [[False] * (n+1) for _ in range(n+1)]
    
    for u, v in results:
        win[u][v] = True
        
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if win[i][k] and win[k][j]:
                    win[i][j] = True
                    
    for i in range(1, n+1):
        cnt = 0
        for j in range(1, n+1):
            if win[i][j] or win[j][i]:
                cnt += 1
        if cnt == n-1:
            answer += 1
            
    return answer
