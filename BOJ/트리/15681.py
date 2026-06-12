import sys
input = sys.stdin.readline
from collections import deque
sys.setrecursionlimit(10**6)

N, R, Q = map(int, input().split())
adj = [[] for _ in range(N+1)]
p = [0] * (N+1)
cnt = [1] * (N+1)

def dfs(cur):
	for nxt in adj[cur]:
		if p[cur] == nxt:
			continue
		p[nxt] = cur
		dfs(nxt)
		cnt[cur] += cnt[nxt]

for _ in range(N-1):
    U, V = map(int, input().split())
    adj[U].append(V)
    adj[V].append(U)
	
ans = []

dfs(R)

for _ in range(Q):
    query = int(input())
    ans.append(str(cnt[query]))

print('\n'.join(ans))