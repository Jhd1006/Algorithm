import sys
input = sys.stdin.readline

T = int(input())

ans = []
for test_case in range(T):
    n = int(input())
    d = {}
    for _ in range(n):
        name, kind = input().split()
        if kind in d:
            d[kind] += 1
        else:
            d[kind] = 1
    result = 1
    for cnt in d.values():
        result *= (cnt+1)
    result -= 1
    ans.append(result)
print('\n'.join(map(str, ans)))

