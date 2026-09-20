def solution(brown, yellow):
    answer = []
    arr = []
    tot = brown + yellow
    
    for i in range(1, int(tot**0.5) + 1):
        if tot % i == 0:
            arr.append((tot//i, i))
            
    for w, h in arr:
        if (w - 2) * (h - 2) == yellow:
            answer = (w, h)
    return answer
