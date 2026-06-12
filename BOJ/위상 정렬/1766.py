import sys
input = sys.stdin.readline
import heapq

N, M = map(int, input().split())
adj = [[] for _ in range(N+1)]
indegree = [0] * (N+1)

for _ in range(M):
    A, B = map(int, input().split())
    adj[A].append(B)
    indegree[B] += 1

h = []

for i in range(1, N+1):
    if indegree[i] == 0:
        heapq.heappush(h, i)

ans = []
while h:
    cur = heapq.heappop(h)
    ans.append(cur)
    for nxt in adj[cur]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            heapq.heappush(h, nxt)
print(' '.join(map(str, ans)))
