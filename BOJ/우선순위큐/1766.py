import sys
input = sys.stdin.readline
import heapq

N, K = map(int, input().split())
bags = []
jewels = []
pq = []

for _ in range(N):
    M, V = map(int, input().split())
    jewels.append((M, V))
jewels.sort()

for _ in range(K):
    C = int(input())
    bags.append(C)
bags.sort()

ans = 0
idx = 0

for bag in bags:
    while idx < N and jewels[idx][0] <= bag:
        heapq.heappush(pq, -jewels[idx][1])
        idx += 1
    if pq:
        ans -= heapq.heappop(pq)

print(ans)


# for bag in bags:
#     if pq:
#         if bag >= -pq[0][1]:
#             ans -= heapq.heappop(pq)[0]
#         else:

# print(ans)

# ans = 0
# while bags:
#     if bags[0] > jewels[0][1]:
#         heapq.heappop(jewels)
#     ans -= heapq.heappop(jewels)[0]
#     heapq.heappop(bags)

# print(ans)


# 보석 M 무게 V 가격
# 가방 최대 무게 C

# ans = 보석 최대 가격