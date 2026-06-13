# from functools import cmp_to_key

# def func(a, b):
#     if a + b > b + a:
#         return -1
#     elif a + b < b + a:
#         return 1
#     return 0

# def solution(numbers):
#     numbers = list(map(str, numbers))
#     sorted_numbers = sorted(numbers, key = cmp_to_key(func))
#     answer = ''
#     answer= ''.join(sorted_numbers)
#     if answer[0] == '0':
#         return '0'
#     return answer

# 다른 풀이
# 원소가 1000 이하, 4번 반복하여 비교
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x : (x * 4), reverse = True)
    answer = ''.join(numbers)
    if answer[0] == '0':
        return '0'
    return answer
    return answer
