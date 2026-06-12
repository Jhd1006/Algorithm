import sys
input = sys.stdin.readline

S = input().strip()
substr = set()
for i in range(len(S)):
    for j in range(i+1, len(S)+1):
        substr.add(S[i:j])
print(len(substr))
