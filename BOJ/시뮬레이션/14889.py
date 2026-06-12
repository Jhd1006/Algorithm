# import sys
# input = sys.stdin.readline
# from itertools import combinations

# N = int(input().strip())

# S = [list(map(int, input().split())) for _ in range(N)]

# ans = float('inf')
# players = list(range(N))
# half = N //2
# comb = list(combinations(players, half))
# for start in comb[:len(comb)//2]:
#     link = [l for l in players if l not in start]
#     score_s = sum(S[i][j] + S[j][i] for i, j in combinations(start, 2))
#     score_l = sum(S[i][j] + S[j][i] for i, j in combinations(link, 2))
#     diff = abs(score_s - score_l)
#     ans = min(ans, diff)
# print(ans)

import sys
input = sys.stdin.readline
from itertools import combinations

N = int(input().strip())

S = [list(map(int, input().split())) for _ in range(N)]

ans = float('inf')
players = list(range(N))
half = N//2

comb = list(combinations(players, half))

for start in comb[:len(comb)//2]:
    link = [l for l in players if l not in start]
    sscore = sum(S[i][j] + S[j][i] for i, j in combinations(start, 2))
    lscore = sum(S[i][j] + S[j][i] for i, j in combinations(link, 2))
    diff = abs(sscore - lscore)
    ans = min(ans, diff)
print(ans)