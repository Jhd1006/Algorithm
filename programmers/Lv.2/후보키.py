from itertools import combinations

def solution(relation):
    answer = 0
    col = len(relation[0])
    row = len(relation)
    found = []

    for i in range(1, col + 1):
        for comb in combinations(range(col), i):
            is_min = True
            for f in found:
                if set(f) <= set(comb):
                    is_min = False
                    break
            if not is_min:
                continue 
                
            s = set()
            for r in range(row):
                tup = tuple(relation[r][c] for c in comb)
                s.add(tup)
                
            if len(s) == row:
                answer += 1
                found.append(comb)          
                    
    return answer
