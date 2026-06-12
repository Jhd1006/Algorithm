import sys
input = sys.stdin.readline

idx = [0] * 6
def lotto(cur, k, s):  
    if cur == 6:
        case.append(' '.join(map(str, [s[i] for i in idx])))
        return
    start = 0 if cur == 0 else idx[cur-1] + 1 
    for i in range(start, k):
        idx[cur] = i
        lotto(cur+1, k, s)

ans = []
while True:
    case = []
    data = list(map(int, input().split()))
    K = data[0]
    if K == 0:
        break
    S = data[1:]
    S.sort()
    lotto(0, K, S)
    ans.append('\n'.join(case))

print('\n\n'.join(ans))
    
    

