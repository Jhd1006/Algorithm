from itertools import product
def solution(word):
    answer = 0
    w = "AEIOU"
    words = []
    for i in range(6):
        for p in product(w, repeat = i):
            words.append(''.join(p))
    words = sorted(words)
    print(words)
    for i in range(len(words)):
        if words[i] == word:
            answer = i
    return answer


# 권장 코드
# cur이 A, AA, AAA, ... 이런식
# def solution(word):
#     alphabets = ['A', 'E', 'I', 'O', 'U']
#     words = []
#     def dfs(cur):
#         if len(cur) > 5:
#             return
#         if cur:
#             words.append(cur)
#         for a in alphabets:
#             dfs(cur + a)
#     dfs("")
#     return words.index(word) + 1