def check(log):
    stack = []
    for l in log:
        if l == '(':
            stack.append(l)
        else:
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0


def solution(p):
    answer = ""
    if not p:
        return ""
    u, v = "", ""
    left = 0
    right = 0

    for i in range(len(p)):
        if p[i] == '(':
            left += 1
        else:
            right += 1
        if left == right:
            u = p[:i+1]
            v = p[i+1:]
            break
            
    if check(u):
        return u + solution(v)
    
    else:
        answer = '(' + solution(v) + ')'
        deleted = u[1:-1]
        for d in deleted:
            if d == '(':
                answer += ')'
            else:
                answer += '('
        
    return answer
