import sys
input = sys.stdin.readline

points = []
N = int(input())

for _ in range(N):
    x, y = map(int, input().split())
    points.append((x, y))


sorted_points = sorted(points, key = lambda x: (x[1], x[0]))

for point in sorted_points:
    print(f"{point[0]} {point[1]}")
