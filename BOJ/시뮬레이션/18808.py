import sys 
input = sys.stdin.readline

N, M, K = map(int, input().split())

notebook = [[0] * M for _ in range(N)]

def is_stickable(x, y, r, c, sticker):
    for i in range(r):
        for j in range(c):
            if notebook[x+i][y+j] == 1 and sticker[i][j] == 1:
                return False
    return True

def stick(x, y, r, c, sticker):
    for i in range(r):
        for j in range(c):
            if sticker[i][j] == 1:
                notebook[x+i][y+j] = 1


def rotate(r, c, sticker):
    rotated = [[sticker[r-1-j][i] for j in range(r)] for i in range(c)]
    # for i in range(c):
    #     for j in range(r):
    #         rotated[i][j] = sticker[r-1-j][i]
    return rotated

for _ in range(K):
    r, c = map(int, input().split())
    sticker = [list(map(int, input().split())) for _ in range(r)]
    for _ in range(4):
        is_sticked = False
        for x in range(N-r+1):
            if is_sticked:
                break
            for y in range(M-c+1):
                if is_stickable(x, y, r, c, sticker):
                    is_sticked = True
                    stick(x, y, r, c, sticker)
                    break
        if is_sticked:
            break
        sticker = rotate(r, c, sticker)
        r, c = c, r
cnt = 0
for i in range(N):
    for j in range(M):
        if notebook[i][j] == 1:
            cnt += 1
print(cnt)

