import sys
input = sys.stdin.readline
import heapq

N = int(input())

pq = []
for _ in range(N):
    x = int(input())
    heapq.heappush(pq, x)

ans = 0

while len(pq) >= 2:
    tmp_1 = heapq.heappop(pq)
    tmp_2 = heapq.heappop(pq)
    tmp = tmp_1 + tmp_2
    ans += (tmp_1 + tmp_2)
    heapq.heappush(pq, tmp_1 + tmp_2) 

print(ans)