import sys
input = sys.stdin.readline

paren = input().rstrip()
s = []
ans = 0
current = 1
isOk = True
prev = ''

for i in range(len(paren)):
    p = paren[i]
    if p == '(':
        s.append(p)
        current *= 2
    elif p == '[':
        s.append(p)
        current *= 3
    elif p == ')':
        if not s or s[-1] != '(':
            isOk = False
            break
        if paren[i-1] == '(':
            ans += current
        s.pop()
        current //= 2
    elif p == ']':
        if not s or s[-1] != '[':
            isOk = False
            break
        if paren[i-1] == '[':
            ans += current
        s.pop()
        current //= 3

if s:
    isOk = False

print(ans if isOk else 0)