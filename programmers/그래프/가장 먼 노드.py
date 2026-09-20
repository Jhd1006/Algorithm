from collections import deque

def solution(n, edge):
    answer = 0
    adj = [[] for _ in range(n+1)]
    for u, v in edge:
        adj[u].append(v)
        adj[v].append(u)
    def bfs(start):
        dist = [-1] * (n+1)
        dist[start] = 0
        q = deque([start])
        while q:
            cur = q.popleft()
            for nxt in adj[cur]:
                if dist[nxt] != -1:
                    continue
                dist[nxt] = dist[cur] + 1
                q.append(nxt)
        return dist
    dist = bfs(1)
    mx = max(dist)
    answer = dist.count(mx)
    return answer
