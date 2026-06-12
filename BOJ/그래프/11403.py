import sys
input = sys.stdin.readline
from collections import deque

N = int(input())

adj = [list(map(int, input().split())) for _ in range(N)]

def bfs(i):
    vis = [0] * (N)
    q = deque([i])
    while q:
        cur = q.popleft()
        for nxt in range(N):
            if adj[cur][nxt] == 0 or vis[nxt] == 1:
                continue
            q.append(nxt)
            vis[nxt] = 1
    return vis

ans = [[] for _ in range(N)]

for i in range(N):
    ans[i] = bfs(i)
print("===========")
for i in range(N):
    print(' '.join(map(str, ans[i])))


# def get_reachable_row(start):
#     # start 노드에서 갈 수 있는 모든 노드를 담은 한 줄(row)을 반환
#     vis = [0] * N  # 1과 0으로 표현하기 위해 0으로 초기화
#     q = deque([start])
    
#     while q:
#         cur = q.popleft()
#         for nxt in range(N):
#             if adj[cur][nxt] == 1 and not vis[nxt]:
#                 vis[nxt] = 1
#                 q.append(nxt)
#     return vis

# # BFS를 딱 N번만 호출합니다.
# for i in range(N):
#     result_row = get_reachable_row(i)
#     print(*(result_row))