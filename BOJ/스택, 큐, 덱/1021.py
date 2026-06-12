import sys
from collections import deque

input = sys.stdin.readline

ans = 0
N, M = map(int, input().split())
dq = deque(range(1, N+1))
numbers = list(map(int, input().split()))

for num in numbers:
    while (dq[0] != num):
        idx = dq.index(num)
        if idx < len(dq) - idx:
            dq.append(dq.popleft())
            ans += 1
        else :
            dq.appendleft(dq.pop())
            ans += 1
    dq.popleft()
print(ans)


