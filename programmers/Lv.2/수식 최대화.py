from itertools import permutations

def solution(expression):
    answer = 0
    seq = []
    cur_num = 0
    
    def cal(x, y, op):
        if op == '+':
            return x + y
        elif op == '*':
            return x * y
        elif op == '-':
            return x - y
           
    for e in expression:
        if e == '+' or e == '-' or e == '*':
            seq.append(cur_num)
            seq.append(e)
            cur_num = 0
        else:
            cur_num = (cur_num * 10) + int(e)
    seq.append(cur_num)
    
    for order in permutations(['+', '-', '*']):
        arr = seq[:]
        for op in order:
            stack = []
            idx = 0
            while idx < len(arr):
                if arr[idx] == op:
                    cur = stack.pop()   
                    stack.append(cal(cur, arr[idx+1], op))
                    idx += 2
                else:
                    stack.append(arr[idx])
                    idx += 1
            arr = stack
        answer = max(answer, abs(stack[-1]))
    
    return answer
