def solution(want, number, discount):
    answer = 0
    d = {}
    n = sum(number)
    len_d = len(discount)
    cnt = 0
            
    for x in want:
        d[x] = 0

    for i in range(n):
        if discount[i] in d:
            d[discount[i]] += 1 

    for i in range(len_d - n + 1):
        if list(d.values()) == number:
            cnt += 1
        if i == len_d - n:
            break
        if discount[i] in d:
            d[discount[i]] -= 1
        if discount[i+n] in d:
            d[discount[i+n]] += 1
    
    answer = cnt   

    return answer

============================================== ## Counter 사용 ## ==============================================

from collections import Counter

def solution(want, number, discount):
    answer = 0
    tot = sum(number)
    d = len(discount)
            
    item = {w : n for w, n in zip(want, number)}
    
    for i in range(d - tot + 1):
        window = Counter(discount[i:i+tot])
        if window == item:
            answer += 1

    return answer
