import sys
import heapq
input = sys.stdin.readline

T = int(input())

result = []
for _ in range(T):
    K = int(input())
    ans = 0
    pq = []
    sizes = list(map(int, input().split()))
    for s in sizes:
        heapq.heappush(pq, s)
    while len(pq) >= 2:
        tmp1 = heapq.heappop(pq)
        tmp2 = heapq.heappop(pq)
        tmp = tmp1 + tmp2
        ans += tmp
        heapq.heappush(pq, tmp)
    result.append(str(ans))

print('\n'.join(result))