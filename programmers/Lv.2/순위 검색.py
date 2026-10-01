from itertools import combinations
from collections import defaultdict
from bisect import bisect_left

def solution(info, query):
    answer = []
    infos = defaultdict(list)
    
    for person in info:
        person_info = person.split()
        score = int(person_info[-1])
        contents = person_info[:-1]
    
        for i in range(5):
            for comb in combinations(range(4), i):
                tmp_contents = contents[:]
                for idx in comb:
                    tmp_contents[idx] = '-'
                keys = "".join(tmp_contents)
                infos[keys].append(score)   
                
    for key in infos:
        infos[key].sort()
    
    for q in query:
        q_list = q.replace("and ", "").split()
        key = "".join(q_list[:-1])
        score = int(q_list[-1])
        
        if key in infos:
            scores = infos[key]
            cnt = len(scores) - bisect_left(scores, score)
            answer.append(cnt)
        
        else:
            answer.append(0)
        
            
    return answer
