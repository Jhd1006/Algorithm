import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))

for _ in range(m):
    a.sort()
    tmp = a[0] + a[1] 
    a[0], a[1] = tmp, tmp
print(sum(a))