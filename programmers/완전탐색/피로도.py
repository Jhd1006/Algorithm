from itertools import permutations

def solution(k, dungeons):
    answer = -1
    l = len(dungeons)
    mx = 0
    for d in permutations(dungeons, l):
        cnt = 0
        cur = k
        for i in range(l):
            if cur >= d[i][0]:
                cnt += 1
                cur -= d[i][1]
            else:
                break
        mx = max(mx, cnt)
        if mx == l:
            break
    answer = mx
    return answer