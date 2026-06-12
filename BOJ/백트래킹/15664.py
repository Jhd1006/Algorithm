import sys
input = sys.stdin.readline

n, m = map(int, input().split())
seq = list(map(int, input().split()))
seq.sort()
idx = [0]*m

def func(cur):
    if cur == m:
        for i in range(m):
            print(seq[idx[i]], end = ' ')
        print()
        return   
    tmp = None
    if cur == 0:
        start = 0    
    else :
        start = idx[cur-1] + 1 
    for i in range(start, n):
        if seq[i] == tmp:
            continue
        idx[cur] =  i
        tmp = seq[i]
        func(cur+1)
        
func(0)

# 4 2
# 9 7 9 1

# 1 7
# 1 9
# 7 9
# 9 9