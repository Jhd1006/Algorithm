def solution(diffs, times, limit):
    answer = 0
    left, right = 1, max(diffs)
    
    while left <= right:
        level = (left + right) // 2
        result = 0
        for i in range(len(diffs)):
            if diffs[i] <= level:
                result += times[i]
            else:
                retry = (diffs[i] - level)
                time_prev = times[i -1] if i > 0 else 0
                result += retry * (times[i] + time_prev) + times[i]
        if result <= limit:
            right = level - 1
        else:
            left = level + 1
    answer = left
