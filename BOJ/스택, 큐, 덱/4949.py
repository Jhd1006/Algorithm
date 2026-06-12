import sys
input = sys.stdin.readline

result = []
while True:
    line = input().rstrip('\n')
    if line == '.': 
        break
    s = []
    isBalanced = True
    for l in line:
        if (l == '[' or l == '('):
            s.append(l)
        elif (l == ']'):
            if not s or s[-1] != '[':
                isBalanced = False
                break
            s.pop()
        elif (l == ')'):
            if not s or s[-1] != '(':
                isBalanced = False
                break
            s.pop()
    if s:
        isBalanced = False
    result.append('yes' if isBalanced else 'no')
print('\n'.join(result))

