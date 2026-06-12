import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
adj = [[] for _ in range(N+1)]
for _ in range(M):
    q = deque()
    A, B = map(int, input().split())
    adj[B].append(A)

def bfs(start):
    q = deque([start])
    vis = [False] * (N+1)
    vis[start] = True
    cnt = 1
    while q:
        cur = q.popleft()
        for nxt in adj[cur]:
            if vis[nxt]:
                continue
            vis[nxt] = True
            q.append(nxt)
            cnt += 1
    return cnt

ans = []
for i in range(1, N+1):
    ans.append(bfs(i))
mx = max(ans)

result = [str(i) for i, v in enumerate(ans, start = 1) if v == mx]
print(' '.join(result))