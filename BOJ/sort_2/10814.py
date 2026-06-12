import sys
input = sys.stdin.readline

N = int(input())

arr=[]
for _ in range(N):
    age, name = input().split()
    arr.append((age, name))
arr.sort(key=lambda x: int(x[0]))

for a in arr:
    print(f"{a[0]} {a[1]}")