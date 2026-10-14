def solution(targets):
    answer = 0
    targets.sort(key = lambda x : x[1])
    cur = -1
    for start, end in targets:
        if start >= cur:
            answer += 1
            cur = end
    return answer
