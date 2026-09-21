def solution(numbers):
    l = len(numbers)
    answer = [-1] * l
    stack = []
    
    for i in range(l-1, -1, -1):
        while stack and numbers[i] >= stack[-1]:
            stack.pop()
        if stack:
            answer[i] = stack[-1]
        stack.append(numbers[i])
    return answer
