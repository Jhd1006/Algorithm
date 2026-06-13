def solution(nums):
    answer = 0
    kinds = len(set(nums))
    answer = min(len(nums)/2, kinds)
    return answer