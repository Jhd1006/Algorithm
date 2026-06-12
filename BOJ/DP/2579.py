import sys
input = sys.stdin.readline

n = int(input().strip())
score = [list([0]*3)for _ in range(n+2)]
stair=[0]*(n+2)
for i in range(n):
    x = int(input().strip())
    stair[i+1] = x
score[1][1], score[1][2], score[2][1], score[2][2] = stair[1], 0, stair[2], stair[1]+stair[2] 
for i in range(3, n+1):
    score[i][1] = max(score[i-2][1], score[i-2][2]) + stair[i]
    score[i][2] = score[i-1][1] + stair[i]
mx = max(score[n][1], score[n][2])
print(mx)
