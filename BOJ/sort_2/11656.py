import sys
input = sys.stdin.readline

word = input().strip()
arr = []
for i in range(len(word)):
    arr.append(word[i:])
arr.sort()
for a in arr:
    print(a)