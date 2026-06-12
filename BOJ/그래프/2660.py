import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
adj = [[] for _ in range(N+1)]

while True:
    u, v = map(int, input().split())
    if (u , v) == (-1, -1):
        break
    adj[u].append(v)
    adj[v].append(u)

scores = []
def bfs(start):
    dist = [-1] * (N+1)
    q = deque([start])
    dist[start] = 0
    while q:
        cur = q.popleft()
        for nxt in adj[cur]:
            if dist[nxt] != -1:
                continue
            dist[nxt] = dist[cur] + 1
            q.append(nxt)
    scores.append(max(dist)) 

for i in range(1, N+1):
    bfs(i)

mn = min(scores)
print(mn, scores.count(mn))

ans = [idx for idx , score in enumerate(scores, start = 1) if score == mn]
print(*ans)
# ans = []
# for i in range(N):
#     if scores[i] == mn:
#         ans.append(i+1)

# print(' '.join(map(str, ans)))


    