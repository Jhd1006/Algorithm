import sys
import heapq
input = sys.stdin.readline

N = int(input())

pq = []


for _ in range(N):
    nums = list(map(int, input().split()))
    for num in nums:
        heapq.heappush(pq, num)
        if len(pq) > N:
            heapq.heappop(pq)
print(pq[0])


