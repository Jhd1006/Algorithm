import sys
input = sys.stdin.readline
from itertools import combinations

N, M= map(int, input().split())

city = [list(map(int, input().split())) for _ in range(N)]
chicken = []
house = []


for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            house.append((i,j))
        elif city[i][j] == 2:
            chicken.append((i, j))
chickens = list(combinations(chicken, M))

ans = float('inf')
for c in chickens:
    city_dist = 0
    for h in house:
        hx, hy = h
        home_dist = min(abs(cx-hx) + abs(cy-hy) for cx, cy in c)
        city_dist += home_dist
    ans = min(ans, city_dist)

print(ans)
