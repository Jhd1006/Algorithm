import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
adj = [[]for _ in range(N+1)]
p = [-1 ] * (N+1)
vis = [False] * (N+1)

def bfs(start):
    q = deque([start])
    vis[start] = True
    while q:
        cur = q.popleft()
        for nxt in adj[cur]:
            if vis[nxt]:
                continue
            q.append(nxt)
            vis[nxt] = True


for _ in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

cnt = 0
for i in range(1, N+1):
    if vis[i]:
        continue
    bfs(i)
    cnt += 1
 
print((cnt-1) + (M-(N-cnt)))
# def bfs(start):
#     if vis[start]:
#         return 0
#     cnt = 1
#     q = deque([start])
#     vis[start] = True
#     while q:
#         cur = q.popleft()
#         for nxt in adj[cur]:
#             if p[cur] == nxt:
#                 continue
#             if vis[nxt]:
#                 cnt += 1
#                 continue
#             p[nxt] = cur
#             q.append(nxt)
#             vis[nxt] = True
#     return cnt


# for _ in range(M):
#     u, v = map(int, input().split())
#     adj[u].append(v)
#     adj[v].append(u)

# ans = 0
# for i in range(1, N+1):
#     ans += bfs(i)

# print(ans-1)
# 4 2 
# 1 2
# 3 4


# void bfs(int cur) {
#     queue<int> Q;
#     Q.push(cur);
#     vis[cur] = true;
#     while (!Q.empty()) {
#         int cur = Q.front();
#         Q.pop();
#         for (int nxt : adj[cur]) {
#             if (vis[nxt]) continue;
#             Q.push(nxt);
#             vis[nxt] = true;
#         }
#     }
# }

# int main(void) {
#     ios::sync_with_stdio(0);
#     cin.tie(0);
#     int u, v, d;
#     int cnt = 0;
#     cin >> N >> M;
#     for (int i = 0; i < M; i++) {
#         cin >> u >> v;
#         adj[u].push_back(v);
#         adj[v].push_back(u);
#     }
#     for (int i = 1; i <= N; i++) {
#         if (vis[i]) continue;
#         bfs(i);
#         cnt++;
#     }
#     cout << (cnt - 1) + (M - (N - cnt));
# }