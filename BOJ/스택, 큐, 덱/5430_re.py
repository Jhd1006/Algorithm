import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
result = []
for _ in range(T):
    isReverse = False
    isError = False
    p = input().strip()
    n = int(input())
    #arr = input().strip().strip('[]')
    line = input().strip()
    dq = deque()
    if line != '[]':
        arr = line[1:-1]
        dq = deque(arr.split(',')) 
    for cmd in p:
        if cmd == 'R':
            isReverse = not isReverse
        elif cmd == 'D':
            if not dq:
                isError = True
                break
            else:
                if isReverse:
                    dq.pop()
                else:
                    dq.popleft()
    if isError:
        result.append('error')
    else:
        if isReverse:
            dq.reverse()
        result.append('[' + ','.join(dq) + ']')
print('\n'.join(result))