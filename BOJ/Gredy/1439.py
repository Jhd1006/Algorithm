# 11001100110011000001
# 4

import sys
input = sys.stdin.readline

S = input().strip()
cnt = [0, 0]
cnt[int(S[0])] = 1
for i in range(1, len(S)):
    if S[i] != S[i-1]:
        cnt[int(S[i])] += 1
print(min(cnt))