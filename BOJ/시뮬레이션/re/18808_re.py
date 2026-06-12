import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
notebook = [[0]*M for _ in range(N)]
def is_stickable(x, y, R, C, sticker):
    for i in range(R):
        for j in range(C):
            if sticker[i][j] == 1 and notebook[x+i][y+j] == 1:
                return False
    return True

def stick(x, y, R, C, sticker):
    for i in range(R):
        for j in range(C):
            if sticker[i][j] == 1:
                notebook[x+i][y+j] = 1

def rotate(R, C, sticker):
    rotated = [[sticker[R-1-j][i] for j in range(R)] for i in range(C)]
    return rotated
    


for _ in range(K):
    R, C = map(int, input().split())
    sticker = [list(map(int, input().split())) for _  in range(R)]
    for _ in range(4):
        is_sticked = False
        for x in range(N-R+1):
            if is_sticked:
                break
            for y in range(M-C+1):
                if is_stickable(x, y, R, C, sticker):
                    is_sticked = True
                    stick(x, y, R, C, sticker)
                    break
        if is_sticked:
            break
        sticker = rotate(R, C, sticker)
        R, C = C, R
cnt = 0
for i in range(N):
    for j in range(M):
        if notebook[i][j] == 1:
            cnt += 1
print(cnt)