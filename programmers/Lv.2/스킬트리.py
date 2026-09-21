def solution(skill, skill_trees):
    answer = 0
    
    for st in skill_trees:
        idx = 0
        for s in st:
            if s in skill:
                if s == skill[idx]:
                    idx += 1
                else:
                    break
        else:
            answer += 1        
            
    return answer
