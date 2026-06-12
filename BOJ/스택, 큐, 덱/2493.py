import sys
input = sys.stdin.readline

N = int(input())
heights = list(map(int, input().split()))
tower = []
ans=[]

for i in range(N):
    h = heights[i]
    while tower and tower[-1][1] < h:
        tower.pop()
    if not tower:
        ans.append(0)
    else:
        ans.append(tower[-1][0])
    tower.append((i+1, h))

print(' '.join(map(str,ans)))
