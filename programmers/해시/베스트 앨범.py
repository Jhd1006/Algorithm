# def solution(genres, plays):
#     answer = []
#     genre_set = set(genres)
#     d = {}
#     for gs in genre_set:
#         d[gs] = []
#     for i in range(len(genres)):
#         d[genres[i]].append((i, plays[i]))
#     for gs in genre_set:
#         d[gs].sort(key = lambda x : x[1], reverse = True)
#     sum_d = {}
#     for k in d.keys():
#         sum_d[k] = sum(x[1] for x in d[k])
#     genre_order = sorted(sum_d, key = lambda x : sum_d[x], reverse = True)
#     print(d)
#     for g in genre_order:
#         for num, cnt in d[g][:2]:
#             answer.append(num)
#     return answer

from collections import defaultdict

def solution(genres, plays):
    dd_sum = defaultdict(int)
    dd = defaultdict(list)
    for i, (g, p) in enumerate(zip(genres, plays)):
        dd_sum[g] += p
        dd[g].append((p, i))
    answer = []
    dd_sum = sorted(dd_sum, key = lambda x : dd_sum[x], reverse = True)
    for g in dd_sum:
        songs = sorted(dd[g], key = lambda x : (-x[0], x[1]))
        for s in songs[:2]:
            answer.append(s[1])
    return answer


# 1) 노래 많이 재생된 장르부터
# 2) 많이 재생된 노래부터
# 3) 고유번호 낮은 노래부터
# 4) 한 장르당 최대 2곡