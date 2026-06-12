import sys
input = sys.stdin.readline
s = []
cnt = 0
prev = ''
stick = input().rstrip('\n')
for c in stick:
    if c == '(':
        s.append(c)
    else:
        s.pop()
        if prev == '(':
            cnt += len(s)
        elif prev == ')':
            cnt += 1
    prev = c

print(cnt)

# ()(((()())(())()))(()) 17
# 3 3 3 2 2 2 2