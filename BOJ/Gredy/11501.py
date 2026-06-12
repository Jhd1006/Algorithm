import sys
input = sys.stdin.readline

T = int(input())
ans = []
for _ in range(T):
    N = int(input())
    price = list(map(int, input().strip().split())) 
    cnt = 0
    mx = 0
    for i in range(N-1, -1, -1):
        mx = max(mx, price[i])
        if mx > price[i]:
            cnt += (mx-price[i])
    ans.append(str(cnt))
print('\n'.join(ans))