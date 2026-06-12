import sys
input = sys.stdin.readline
import heapq

n = int(input())
m = int(input())

inf = float('inf')
d = [inf] * (n+1)
pre = [0] * (n+1)
adj = [[] for _ in range(n+1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    adj[u].append((w, v))

start, end = map(int, input().split())
pq = []
d[start] = 0
heapq.heappush(pq, (d[start], start))

while pq:
    cur = heapq.heappop(pq)
    if d[cur[1]] != cur[0]:
        continue
    for nxt in adj[cur[1]]:
        if d[nxt[1]] <= d[cur[1]] + nxt[0]:
            continue
        d[nxt[1]] = d[cur[1]] + nxt[0]
        heapq.heappush(pq, (d[nxt[1]], nxt[1]))
        pre[nxt[1]] = cur[1]

print(d[end])

path = []
cur = end
while cur != start:
    path.append(cur)
    cur = pre[cur]
path.append(cur)

path.reverse()
print(len(path))
print(' '.join(map(str, path)))