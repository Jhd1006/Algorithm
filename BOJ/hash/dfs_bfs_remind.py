def dfs(x):
    visited[x] = True
    for nx in graph[x]:
        if not visited[nx]:
            dfs(nx)

from collections import deque

def bfs(start):
    q = deque([start])
    visited[start] = True
    
    while q:
        x = q.popleft()
        for nx in graph[x]:
            if not visited[nx]:
                visited[nx] = True
                q.append(nx)
