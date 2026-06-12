import sys
input = sys.stdin.readline
from itertools import combinations

N = int(input().strip())
S = [list(map(int, input().split())) for _ in range(N)]

players = list(range(N))
half = N // 2
comblist = list(combinations(players, half))
halfcomb = comblist[:len(comblist)//2]

ans = float('inf')

# 리스트 컴프리헨션 쓴다면

for s in halfcomb:
    l = [x for x in players if x not in s]
    sscore = sum(S[i][j] + S[j][i] for i,j in combinations(s, 2))
    lscore = sum(S[i][j] + S[j][i] for i,j in combinations(l, 2))
    diff = abs(sscore - lscore)
    ans = min(ans, diff)

# for 반복 + append 쓴다면 

for s in halfcomb:
    l=[]
    for x in players:
        if x not in s:
            l.append(x)
    sscore = sum(S[i][j] + S[j][i] for i,j in combinations(s, 2))
    lscore = sum(S[i][j] + S[j][i] for i,j in combinations(l, 2))
    diff = abs(sscore - lscore)
    ans = min(ans, diff)

print(ans)