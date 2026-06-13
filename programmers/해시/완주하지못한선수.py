from collections import Counter

def solution(participant, completion):
    answer = ''
    cp = Counter(participant)
    cc = Counter(completion)
    answer = list(cp-cc)[0]
    return answer
