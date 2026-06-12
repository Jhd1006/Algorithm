import sys
input = sys.stdin.readline
import heapq

N = int(input())

max_pq = []
min_pq = []

ans = []
for _ in range(N):
    x = int(input())
    if len(max_pq) > len(min_pq):
        heapq.heappush(min_pq, x)
    else:
        heapq.heappush(max_pq, -x)
    if min_pq and max_pq:
        if -max_pq[0] > min_pq[0]:
            tmp_min = heapq.heappop(min_pq)
            tmp_max = heapq.heappop(max_pq)
            heapq.heappush(min_pq, -tmp_max)
            heapq.heappush(max_pq, -tmp_min)
    ans.append(str(-max_pq[0]))

print('\n'.join(ans))


