import sys
input = sys.stdin.readline

wheel = [list(input().strip()) for _ in range(4)]

K = int(input().strip())

def clock(l):
    return l[-1:] + l[:-1]

def nclock(l):
    return l[1:] + l[:1]

for _ in range(K):

    dirs = [0] * 4
    num, dir = map(int, input().split())
    idx = num -1
    dirs[idx] = dir

    for i in range(idx, 0, -1):
        if wheel[i][6] != wheel[i-1][2]:
            dirs[i-1] = -dirs[i]
        else:
            break
    for i in range(idx, 3, 1):
        if wheel[i][2] != wheel[i+1][6]:
            dirs[i+1] = -dirs[i]
        else:
            break

    for i in range(4):
        if dirs[i] == 1:
            wheel[i] = clock(wheel[i])
        if dirs[i] == -1:
            wheel[i] = nclock(wheel[i])
ans = 0
for i in range(4):  
    if wheel[i][0] == '1':
        ans += (1 <<  i)

print(ans)