# import sys
# input = sys.stdin.readline

# N = int(input())
# cnt = [0] * 2000001
# for _ in range(N):
#     n = int(input())
#     cnt[n+1000000] += 1
# ans = []
# for i in range(2000001):
#     if cnt[i] != 0:
#         ans.append((str(i-1000000)+'\n')*cnt[i])
# print(''.join(ans))

import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    n = int(input())
    arr.append(n)
        
arr.sort()
print('\n'.join(map(str, arr)))