import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
people = sorted(list(input().split()))
adj = {p: [] for p in people}
deg = {p: 0 for p in people}

M = int(input())

for _ in range(M):
    X, Y = input().split()
    adj[Y].append(X)
    deg[X] += 1

q = deque()
roots = []
for p in people:
    adj[p].sort()
    if deg[p] == 0:
        roots.append(p)

print(len(roots))
print(' '.join(sorted(roots)))

for cur in people:
    ans = []
    print(cur, end = ' ')
    for nxt in adj[cur]:
        if deg[nxt] == (deg[cur] + 1):
            ans.append(nxt)
    print(len(ans), end = ' ')
    print(' '.join(map(str,ans)))
