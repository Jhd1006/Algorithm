import sys
input = sys.stdin.readline
import heapq
N = int(input())

room = []

ends = []

for _ in range(N):
    s, t = map(int, input().split())
    room.append((s,t))
room.sort()


heapq.heappush(ends, room[0][1])
ans = 1
for i in range(1, len(room)):
    if ends[0] > room[i][0]:
        ans += 1
        heapq.heappush(ends, room[i][1])
    else:
        heapq.heappop(ends)
        heapq.heappush(ends, room[i][1])
print(ans)

 
#   int ans = 0; // 필요한 강의실의 최대 개수
#   int curtime = event[0].X; // 현재 시간
#   int cur = 0; // 현재 시간에 열려있는 강의실의 개수
#   int idx = 0; // 현재 보고있는 event에서의 인덱스
#   while(true){
#     while(idx < 2*n && event[idx].X == curtime){
#       cur += event[idx].Y;
#       idx++;      
#     }
#     ans = max(ans, cur);
#     if(idx == 2*n) break;
#     curtime = event[idx].X;    
#   }
#   cout << ans << '\n';
# }

