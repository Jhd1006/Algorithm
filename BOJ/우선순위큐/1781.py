import sys
input = sys.stdin.readline
import heapq

N = int(input())

l = [[] for _ in range(N+1)]
pq = []

for _ in range(N):
    dead, ramen = map(int, input().split())
    l[dead].append(ramen)

ans = 0
today = 1

for date in range(N, 0, -1):
    for r in l[date]:
        heapq.heappush(pq, -r)
    if not pq:
        continue
    ans -= pq[0]
    heapq.heappop(pq)
print(ans)




#   cin >> N;
#   for (int i = 0; i < N; i++) {
#     cin >> dl >> cn;
#     cn_by_deadline[dl].push_back(cn);
#   }
#   for (int curr = 200'001; curr != 0; curr--) {
#     for (int noodle : cn_by_deadline[curr])
#       cn_candidate.push(noodle);

#     if (cn_candidate.empty()) continue;
#     cupNoodles += cn_candidate.top();
#     cn_candidate.pop();
#   }
#   cout << cupNoodles;
# }
