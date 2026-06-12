import sys
input = sys.stdin.readline

N = int(input())
flowers = []
for _ in range(N):
    sm, sd, em, ed = map(int, input().split())
    flowers.append((sm*100 + sd, em*100 + ed))
flowers.sort(key = lambda x : (x[0], -x[1]))

# prev_end = 301
# cnt = 0
# cur = 0

# while prev_end <= 1130:
#     current_end = prev_end
#     while cur < N and flowers[cur][0] <= prev_end:
#         current_end = max(current_end, flowers[cur][1])
#         cur += 1
#     if current_end == prev_end: 
#         print(0)
#         break
#     cnt += 1
#     prev_end = current_end
# else:
#     print(cnt)
prev_end = 301
cnt = 0
cur = 0

while prev_end <= 1130:
    current_end = prev_end
    for i in range(cur, N):
        if flowers[i][0] > prev_end:
            break
        current_end = max(current_end, flowers[i][1])
    cur = i

    if current_end == prev_end: 
        print(0)
        break
    cnt += 1
    prev_end = current_end
else:
    print(cnt)