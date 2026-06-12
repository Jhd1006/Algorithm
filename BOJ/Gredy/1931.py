import sys
input = sys.stdin.readline

N = int(input())
time = []
for i in range(N):
    s, e = map(int, input().split())
    time.append((e, s))
time.sort()

cur, cnt = 0, 0

for i in range(N):
    if cur > time[i][1]:
        continue
    cnt += 1
    cur = time[i][0]
print(cnt)
    