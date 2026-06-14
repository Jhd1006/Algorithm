import math
from itertools import permutations

def solution(numbers):
    answer = 0
    n = 10000000
    is_prime = [True] * (n + 1)
    is_prime[0], is_prime[1] = False, False
    arr = []
    for i in range(2, int(math.sqrt(n)) + 1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    for i in range(1, len(numbers) + 1):
        for p in permutations(numbers, i):
            if p[0] == 0:
                continue
            arr.append(int(''.join(p)))
    arr = set(arr)
    print(arr)
    for a in arr:
        if is_prime[a]:
            answer += 1
    return answer 