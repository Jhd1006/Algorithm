from collections import Counter

def solution(topping):
    answer = -1
    cs = Counter()
    br = Counter(topping)
    
    for t in topping:
        cs.update([t])
        br.subtract([t])
        if br[t] == 0:
            br.pop(t)
        if len(cs) == len(br):
            answer += 1

    answer += 1
    return answer

===================== ## 카운터 하나는 set으로 대체 가능 ## =====================
from collections import Counter

def solution(topping):
    answer = -1
    cs = set()
    br = Counter(topping)
    
    for t in topping:
        cs.add(t)
        br[t] -= 1
        if br[t] == 0:
            br.pop(t)
        if len(cs) == len(br):
            answer += 1

    answer += 1
    return answer
