import sys
from collections import deque

input = sys.stdin.readline

isError = False
ans = []
T = int(input())
dq = deque()

for _ in range(T):
    isError = False
    isReverse = False
    dq = deque()

    cmd = input().strip()
    n = int(input())
    numbers = input().strip()

    if numbers != '[]':
        numbers = numbers.strip('[]')
        dq = deque(numbers.split(','))

    for c in cmd:
        if c == 'D':
            if not dq:
                isError = True
                break
            if isReverse:
                dq.pop()
            else:
                dq.popleft()
        elif c == 'R':
            isReverse = not isReverse
    if isError:
        print('error')
    else:
        if isReverse:
            dq.reverse()
        print('[' + ','.join(dq) +']')



