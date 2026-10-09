def solution(s):
    answer = 0
    l = len(s)
    half = l // 2
    
    if l == 1:
        return 1
    
    for unit in range(1, half + 1):
        result = ""
        prev = s[0:unit]
        cnt = 1
        for start in range(unit, l, unit):
            cur = s[start:start + unit]
            if cur == prev:
                cnt += 1
            else:
                if cnt < 2:
                    result += prev
                else:
                    result += (str(cnt) + prev)
                    prev = cur
                    cnt = 1
        if cnt < 2:
            result += prev
        else:
            result += (str(cnt) + prev)
        answer = min(l, len(result))
        
    return answer
