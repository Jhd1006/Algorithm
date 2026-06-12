import sys
input = sys.stdin.readline
import heapq
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
inf = float('inf')

N, M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]
d = [[inf] * (M+1) for _ in range(N+1)]

pq = []
d[1][1] = 0

heapq.heappush(pq, (d[1][1], 1))
