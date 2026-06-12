import sys
input = sys.stdin.readline

points = []
N = int(input())

for _ in range(N):
    x, y = map(int, input().split())
    points.append((x, y))

points.sort()

for point in points:
    print(f"{point[0]} {point[1]}")

# sorted_points = sorted(points, key = lambda x: (x[0], x[1]))

# for point in sorted_points:
#     print(f"{point[0]} {point[1]}")
