def solution(n, left, right):
    answer = []   
    
    for c in range(left, right + 1):
        a = c // n
        b = c % n
        mx = max(a, b)
        answer.append(mx + 1)

    return answer
