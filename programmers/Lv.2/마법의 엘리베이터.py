def solution(storey):
    answer = 0
    while storey > 0:
        digit = storey % 10
        if digit < 5:
            answer += digit
        elif digit > 5:
            answer += (10 - digit)
            storey += (10 - digit)
        else:
            nxt_digit = (storey // 10) % 10
            answer += 5
            if nxt_digit >= 5:
                storey += 5
                
        storey //= 10
    return answer   
