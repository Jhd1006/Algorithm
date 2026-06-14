def solution(sizes):
    answer = 0
    x, y = 0, 0
    for s in sizes:
        w, h = max(s), min(s)
        x = max(x, w)
        y = max(y, h)
    answer = x * y
    return answer