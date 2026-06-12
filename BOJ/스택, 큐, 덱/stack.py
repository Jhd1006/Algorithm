import sys
# input = sys.stdin.readline

S = []

msg = input("문자열 입력 : ").strip()

for c in msg:
    S.append(c)

print("문자열 출력:", end=' ')
while len(S) > 0:
    print(S.pop(), end=' ')
print()