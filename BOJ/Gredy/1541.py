import sys
input = sys.stdin.readline

S = input().strip()

ans = 0
sign = 1
num = 0
for s in S:
    if s == '-':
        ans += sign*num
        sign = -1
        num = 0
    elif s == '+':
        ans += sign * num
        num = 0
    else:
        num *= 10
        num += int(s) 

print(num*sign+ans)

