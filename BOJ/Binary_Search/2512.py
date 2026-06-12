import sys
input = sys.stdin.readline

N = int(input())
bg = list(map(int, input().split()))
M = int(input())

start, end = 1, max(bg)

def func(target):
   s = sum(min(b, target) for b in bg)
   return s
   
while start <= end:
    mid = (start + end) // 2
    if M >= func(mid):
      start = mid + 1
    else:
       end = mid - 1

print(end)
