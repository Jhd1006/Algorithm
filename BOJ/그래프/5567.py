import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
m = int(input())

adj = [[] for _ in range(n+1)]
dist = [-1] * (n+1
                 )
for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

q = deque([1])
dist[1] = 0
cnt = 0
while q:
    cur = q.popleft()
    if 0 < dist[cur] <= 2:
        cnt += 1
    if dist[cur] == 2:
        continue
    for nxt in adj[cur]:
        if dist[nxt] != -1:
            continue
        dist[nxt] = dist[cur]+1
        q.append(nxt)
print(cnt)

