import sys
input = sys.stdin.readline

N, M = map(int, input().split())

dict = {}
for _ in range(N):
    addr, pw = map(str, input().split())
    dict[addr] = pw

ans = []
for _ in range(M):
    addr = input().strip()
    ans.append(dict[addr])

print('\n'.join(ans))