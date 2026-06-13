def solution(phone_book):
    pb = set(phone_book)
    answer = True
    for p in phone_book:
        for i in range(1, len(p)):
            if p[:i] in pb:
                answer = False
    return answer