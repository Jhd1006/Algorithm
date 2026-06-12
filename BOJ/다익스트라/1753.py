import sys
input = sys.stdin.readline
import heapq

V, E = map(int, input().split())
K = int(input())
adj = [[] for _ in range(V+1)]
inf = float('inf')
d = [inf] * (V+1)

for _ in range(E):
    u, v, w = map(int, input().split())
    adj[u].append((w, v))

pq = []
d[K] = 0
heapq.heappush(pq, (d[K], K))

while pq:
  cur = heapq.heappop(pq)
  if cur[0] != d[cur[1]]:
    continue
  for nxt in adj[cur[1]]:
    if d[nxt[1]] <= d[cur[1]] + nxt[0]:
        continue
    d[nxt[1]] = d[cur[1]] + nxt[0]
    heapq.heappush(pq, (d[nxt[1]], nxt[1]))

for e in d[1:]:
    if e == inf:
        print("INF")
    else:
        print(e)