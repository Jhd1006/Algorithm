# 첫째 줄에 테스트 케이스의 개수 T가 주어진다f. 
# 각 테스트 케이스의 첫째 줄에는 A의 수 N과 B의 수 M이 주어진다. 
# 둘째 줄에는 A의 크기가 모두 주어지며, 셋째 줄에는 B의 크기가 모두 주어진다. 
# 크기는 양의 정수이다. (1 ≤ N, M ≤ 20,000) 
import sys
input = sys.stdin.readline

T = int(input())
ans = []

for _ in range(T):
    arr = []
    N, M = map(int, input().split())
    A = map(int, input().split())
    B = map(int, input().split())
    for a in A:
        arr.append((a, 0))
    for b in B:
        arr.append((b, 1))
    arr.sort()
    tmp = 0
    cnt = 0
    for i in range(len(arr)):
        if arr[i][1] == 0:
            cnt += tmp
        elif arr[i][1] == 1:
            tmp += 1
    ans.append(cnt)
print('\n'.join(map(str,ans)))