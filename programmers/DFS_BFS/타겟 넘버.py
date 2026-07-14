def solution(numbers, target):
    answer = 0
    l = len(numbers)
    def dfs(cur, tot):
        nonlocal answer
        if cur == l:
            if tot == target:
                answer +=  1
            return
        dfs(cur + 1, tot + numbers[cur])
        dfs(cur + 1, tot - numbers[cur])
    dfs(0, 0)
    return answer
