import sys
input = sys.stdin.readline

N = int(input())
cnt = [False] * 2000001
for _ in range(N):
    num = int(input())
    cnt[num+1000000] = True

for i in range(2000000, -1, -1):
    if cnt[i] == True:
        print(i - 1000000)

