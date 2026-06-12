import sys
input = sys.stdin.readline

N, M = map(int, input().split())

trees = list(map(int, input().split()))

start, end = 0, max(trees)

while start <= end:
    mid = (start + end) // 2
    take = sum(t - mid for t in trees if t > mid)

    if take >= M:
        start = mid + 1
    elif take < M:
        end = mid - 1

print(end)
    


# import sys
# input = sys.stdin.readline

# lines = []
# K, N = map(int, input().split())

# for _ in range(K):
#     line = int(input())
#     lines.append(line)

# start, end = 1, max(lines)

# while start <= end:
#     mid = (start + end) // 2
#     cnt = 0
#     for line in lines:
#         cnt += (line // mid)
#     if cnt >= N:
#         start = mid + 1
#     else:
#         end = mid - 1
# print(end)