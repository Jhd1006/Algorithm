import sys
import heapq
input = sys.stdin.readline

pq = []
ans = []

N = int(input())

for _ in range(N):
    x = int(input())
    if x == 0:
        if not pq:
            ans.append(0)
        else:
            ans.append(heapq.heappop(pq)[1])
    else:
        heapq.heappush(pq, (abs(x), x))

print('\n'.join(map(str, ans)))
