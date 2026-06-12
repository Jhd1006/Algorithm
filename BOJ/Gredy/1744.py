import sys
input = sys.stdin.readline

N = int(input())

arr = [int(input()) for _ in range(N)]
neg = []
pos = []
ans = 0
for a in arr:
    if a <= 0:
        neg.append(a)
    elif a > 1:
         pos.append(a)
    elif a == 1:
        ans += 1
pos.sort(reverse=True)
neg.sort()

for i in range(0, len(pos), 2):
    if i < (len(pos)-1):
        ans += pos[i]* pos[i+1]
    else:
        ans += pos[i]
for i in range(0, len(neg), 2):
    if i < (len(neg)-1):
        ans += neg[i]* neg[i+1]
    else:
        ans += neg[i]
print(ans)
# ans = 0
# for i in range(1, N, 2):
#     if arr[i-1] < 0 and arr[i] <= 0 :
#         ans += arr[i-1]*arr[i]
#     elif arr[i-1] > 1 and arr[i] > 1 :
#         ans += arr[i-1]*arr[i]
# for i in range(0, N):

#         ans += arr[i]

# print(ans)