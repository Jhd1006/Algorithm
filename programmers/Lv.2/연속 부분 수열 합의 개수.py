def solution(elements):
    answer = 0
    l = len(elements)
    elements = elements * 2
    s = set()
    
    for i in range(1, l + 1):
        for j in range(l):
            window = elements[j:(j + i)]
            s.add(sum(window))
            
    answer = len(s)
    return answer
