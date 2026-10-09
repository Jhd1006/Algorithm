def solution(n):
    answer = []
    
    def hannoi(start, end, mid, n):
        if n == 1:
            answer.append([start, end])
            return
        hannoi(start, mid, end, n-1)
        answer.append([start, end])
        hannoi(mid, end, start, n-1)
        
    hannoi(1, 3, 2, n)
    return answer
