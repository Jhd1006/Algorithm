from itertools import product

def solution(users, emoticons):
    answer = []
    n = len(emoticons)
    arr = []
    
    def func(pro):
        subs = 0
        tot = 0
        for per, cost in users:
            price = 0
            for i in range(n):
                if pro[i] < per:
                    continue
                price += emoticons[i] * (100 - pro[i]) // 100
                if price >= cost:
                    subs += 1
                    price = 0
                    break
            tot += price
        return arr.append([subs, tot])
    
    for pro in product([10, 20, 30, 40], repeat = n):
        func(pro)
        
    arr.sort()
    answer = arr[-1]
    return answer

======== 추천 코드 ======== (최선의 경우를 갱신)

from itertools import product

def solution(users, emoticons):
    answer = []
    n = len(emoticons)
    best = [0, 0]  
    
    for pro in product([10, 20, 30, 40], repeat = n):
        subs, tot = 0, 0
        for per, cost in users:
            price = 0
            for i in range(n):
                if pro[i] < per:
                    continue
                price += emoticons[i] * (100 - pro[i]) // 100
                if price >= cost:
                    subs += 1
                    price = 0
                    break
            tot += price
        best = max(best, [subs, tot])
        
    answer = best
    return answer
