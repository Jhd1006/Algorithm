def counting(distance, rocks, n, mid):
    removed = 0
    prev = 0
    for r in rocks:
        if r - prev < mid:
            removed += 1
        else:
            prev = r
    if distance - prev < mid:
        removed += 1
    return removed
# removed가 n보다 크지만 않으면 mid 늘릴 수 있음
def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    left, right = 1, distance
    while left <= right:
        mid = (left + right) // 2
        if counting(distance, rocks, n, mid) <= n:
            answer = mid
            left = mid + 1
        else:
            right = mid -1
    return answer
