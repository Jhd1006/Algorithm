import sys
input = sys.stdin.readline

N = int(input())
S = []

for _ in range(N):
    cmd = input().split()
    if cmd[0] == 'push':
        S.append(cmd[1])
    elif cmd[0] == 'pop':
        print(S.pop() if S else -1)
    elif cmd[0] == 'size':
        print(len(S))
    elif cmd[0] == 'empty':
        print(1 if not S else 0)
    else:
        print(S[-1] if S else -1)