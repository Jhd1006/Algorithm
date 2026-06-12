import sys
input = sys.stdin.readline

N = int(input().strip())
board = [list(map(int, input().split()))for _ in range(N)]
mboard = [row[:] for row in board]

def tilt(dir, mboard):
    for i in range(dir):
        mboard = rotate(mboard)
    for i in range(N):
        tilted = [0] * N
        idx = 0
        for j in range(N):
            if mboard[i][j] == 0:
                continue
            if tilted[idx] == 0:
                tilted[idx] = mboard[i][j]
            elif tilted[idx] == mboard[i][j]:
                tilted[idx] *= 2
                idx += 1
            else:
                idx += 1
                tilted[idx] = mboard[i][j]
        mboard[i] = tilted
    return mboard
                

def rotate(mboard):
    rotated = [[mboard[N-1-j][i] for j in range(N)]for i in range(N)]
    return rotated

ans = 0
for tmp in range(1<<(2*5)):
    mboard = [row[:] for row in board]
    brute = tmp
    for _ in range(5):
        dir = brute % 4
        brute //= 4
        mboard = tilt(dir, mboard)
    for i in range(N):
        for j in range(N):
            ans = max(ans, mboard[i][j])
print(ans)