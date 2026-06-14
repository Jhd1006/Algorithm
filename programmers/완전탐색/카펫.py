def solution(brown, yellow):
    answer = []
    arr = []
    tot = brown + yellow
    for i in range(1, int(tot**0.5) + 1):
        if tot % i == 0:
            arr.append((tot //i, i))
    for a in arr:
        if (a[0] - 2) * (a[1] - 2) == yellow:
            answer = a
    return answer