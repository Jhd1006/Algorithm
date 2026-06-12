import sys
input = sys.stdin.readline
import heapq

n = int(input())
l = [[] for _ in range(10001)]
pq = []
mx = 0

for _ in range(n):
    p, d = map(int, input().split())
    l[d].append(p)
    mx = max(mx, d)

ans = 0
for d in range(mx, 0, -1):
    for p in l[d]:
        heapq.heappush(pq, -p)
    if not pq:
        continue
    ans -= heapq.heappop(pq)

print(ans)
