import sys
input = sys.stdin.readline
import heapq

N = int(input())

pq = []
ans = []

for _ in range(N):
    x = int(input())
    if x == 0:
        if not pq:
            ans.append(0)
        else:
            ans.append(heapq.heappop(pq)[1])
    else:
        heapq.heappush(pq, (-x, x))

print('\n'.join(map(str, ans)))
            
