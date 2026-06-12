import sys
import heapq
input = sys.stdin.readline

N = int(input())

pq = []
ans = []

for _ in range(N):
    x = int(input())
    if x == 0:
        if not pq:
            ans.append(0)
        else:
            ans.append(heapq.heappop(pq))
    else:
        heapq.heappush(pq, x)

print('\n'.join(map(str, ans)))


