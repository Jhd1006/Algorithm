import sys
input = sys.stdin.readline
import heapq
V, E = map(int, input().split())

adj = [[] for _ in range(V+1)]
check = [False] * (V+1)
cnt = 0
pq = []

for _ in range(E):
    A, B, C = map(int, input().split())
    adj[A].append((C, B))
    adj[B].append((C, A))

check[1] = True
for nxt in adj[1]:
    heapq.heappush(pq, (nxt[0], nxt[1]))

sum = 0
while cnt < (V-1):
    cost, u = heapq.heappop(pq)
    if check[u]:
        continue
    check[u] = True
    sum += cost
    cnt += 1
    for nxt in adj[u]:
        heapq.heappush(pq, (nxt[0], nxt[1]))

print(sum)


