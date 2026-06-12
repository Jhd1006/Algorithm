import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
l = list(map(int, input().split()))

know = [False] * (N+1)
party = [[] for _ in range(M+1)]
adj = [[] for _ in range(N+1)]

for k in l[1:]:
    know[k] = True

def bfs(start):
    if not know[start]:
        return
    q = deque([start])
    while q:
        cur = q.popleft()
        for nxt in adj[cur]:
            if know[nxt]:
                continue
            q.append(nxt)
            know[nxt] = True

for i in range(1, M+1):
    people = list(map(int, input().split()))
    party[i] = people[1:]
    for j in range(0, len(party[i])-1):
        adj[party[i][j]].append(party[i][j+1])
        adj[party[i][j+1]].append(party[i][j])

for i in range(1, N+1):
    bfs(i)

cnt = 0
for i in range(1, M+1):
    isTrue = False
    for p in party[i]:
        if know[p]:
            isTrue = True
    if not isTrue:
        cnt +=1 
print(cnt)
