from collections import deque

def solution(n, computers):
    answer = 0
    vis = [False] * n
    def bfs(start):
        q = deque([start])
        vis[start] = True
        while q:
            cur = q.popleft()
            for nxt in range(n):
                if computers[cur][nxt] and not vis[nxt]:
                    q.append(nxt)
                    vis[nxt] = True 
    for i in range(n):
        if vis[i]:
            continue
        bfs(i)
        answer += 1
    return answer
