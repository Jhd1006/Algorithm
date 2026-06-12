import sys 
from collections import deque
input = sys.stdin.readline

N = int(input())
q= deque()
ans = []

for _ in range(N):
    cmd = input().split()
    if cmd[0] == 'push':
        q.append(cmd[1])
    elif cmd[0] == 'pop':
        ans.append(q.popleft() if q else '-1')
    elif cmd[0] == 'size':
        ans.append(str(len(q)))
    elif cmd[0] == 'empty':
        ans.append('0' if q else '1')
    elif cmd[0] == 'front':
        ans.append(q[0] if q else '-1')
    else:
        ans.append(q[-1] if q else '-1')
print('\n'.join(ans))