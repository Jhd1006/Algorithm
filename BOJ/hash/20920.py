import sys
input = sys.stdin.readline

voca = {}
N, M = map(int, input().split())
for _ in range(N):
    word = input().strip()
    if len(word) < M:
        continue
    if word in voca:
        voca[word] += 1
    else:
        voca[word] = 1

sorted_voca = sorted(voca.keys(), key = lambda x : (-voca[x], -len(x), x))
# sorted_voca = [s[0] for s in sorted(voca.items(), key = lambda x : (-x[1], -len(x[0]), x[0]))]
print('\n'.join(sorted_voca))

