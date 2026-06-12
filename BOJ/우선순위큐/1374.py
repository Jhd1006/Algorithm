import sys
input = sys.stdin.readline
import heapq

N = int(input())

rooms = []
pq = []
for _ in range(N):
    num, start, end = map(int, input().split())
    rooms.append((start, end)) 

rooms.sort(key = lambda x : x[0])

for room in rooms:
    heapq.heappush(pq, room[1])
    if pq:
        if room[0] >= pq[0]:
            heapq.heappop(pq)

print(len(pq))

# 15 21 / 20 25 / 3 8

