import sys
input = sys.stdin.readline

S, E, Q = input().split()

s = set()
cnt = 0
while True:
    line = input().split()
    if not line:
        break
    time, name = line
    if time <= S:
        s.add(name)
    if E <= time <= Q:
        if name in s:
            cnt += 1
            s.discard(name)


print(cnt)