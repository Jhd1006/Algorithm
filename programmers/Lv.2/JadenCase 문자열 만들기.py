def solution(s):
    answer = ''
    s = list(s)
    l = len(s)
    for i in range(l):
        s[i] = s[i].lower()
    s[0] = s[0].upper()
    for i in range(1, l-1):
        if s[i] == ' ':
            s[i+1] = s[i+1].upper()
    answer = "".join(s)  
    return answer
