import sys
input = sys.stdin.readline

name_to_num = {}
num_to_name = []

ans = []
N, M = map(int, input().split())
for i in range(N):
    name = input().strip()
    name_to_num[name] = i
    num_to_name.append(name)
for _ in range(M):
    q = input().strip()
    if q.isdigit():
        ans.append(num_to_name[int(q)-1])
    else:
        ans.append(str(name_to_num[q]+1))
print('\n'.join(ans))
