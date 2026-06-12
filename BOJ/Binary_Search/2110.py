import sys
input = sys.stdin.readline

N, C = map(int, input().split())

house = []
for _ in range(N):
    x = int(input())
    house.append(x)
print(house)

