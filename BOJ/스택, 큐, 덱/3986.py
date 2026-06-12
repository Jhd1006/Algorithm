import sys
input = sys.stdin.readline

N = int(input())
cnt = 0
for _ in range(N):
    s = []
    words = input().rstrip('\n')
    for w in words:
        if s and s[-1] == w:
            s.pop()
        else:
            s.append(w) 
    if not s:
        cnt += 1

print(cnt)