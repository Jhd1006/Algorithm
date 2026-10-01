from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    
    for c in course:
        counter = Counter()
        for o in orders:
            o = sorted(o)
            for comb in combinations(o, c):
                menu = ''.join(comb)
                counter[menu] += 1   
        if not counter:
            continue
        mx = max(counter.values())
        if mx >= 2:
            answer += [menu for menu, cnt in counter.items() if cnt == mx]
    
    answer.sort()
    return answer
