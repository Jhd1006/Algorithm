import sys
input = sys.stdin.readline
import heapq

N, M, X = map(int, input().split())
adj = [[] for _ in range(N+1)]
rev = [[] for _ in range(N+1)]
inf = float('inf')

for _ in range(M):
    u, v, T = map(int, input().split())
    adj[u].append((T, v))
    rev[v].append((T, u))


def dijkstra(start, adj):
    pq = []
    d = [inf] * (N+1)
    d[start] = 0
    heapq.heappush(pq, (d[start], start))
    while pq:
        cur = heapq.heappop(pq)
        if cur[0] != d[cur[1]]:
            continue
        for nxt in adj[cur[1]]:
            if d[nxt[1]] <= d[cur[1]] + nxt[0]:
                continue
            d[nxt[1]] = d[cur[1]] + nxt[0]
            heapq.heappush(pq, (d[nxt[1]], nxt[1]))
    return d

p_to_s = dijkstra(X, adj)
s_to_p =  dijkstra(X, rev)

mx = 0
for i in range(1, N+1):
    mx = max(mx, p_to_s[i] + s_to_p[i])
print(mx)