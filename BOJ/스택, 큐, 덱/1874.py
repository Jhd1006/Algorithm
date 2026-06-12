import sys
input = sys.stdin.readline

n = int(input())
s = []
result = []
possible = True
x = 1

for _ in range(n):
    k = int(input())
    while x <= k:
        s.append(x)
        result.append('+')
        x += 1
    if s[-1] == k:
        s.pop()
        result.append('-')
    else:
        possible = False
        break

print('\n'.join(result) if possible else 'NO')

