import sys
input = sys.stdin.readline

N = int(input())

lines = []
for _ in range(N):
    x, y = map(int, input().split())
    lines.append((x, y))

lines.sort()
cur_x, cur_y = lines[0]

ans = 0
for i in range(1, N):
    start, end = lines[i]
    if start <= cur_y:
        cur_y = max(cur_y, end)
    else:
        ans += cur_y - cur_x
        cur_x, cur_y = start, end
ans += (cur_y - cur_x)
print(ans)

# int main(void) {
#   ios::sync_with_stdio(0);
#   cin.tie(0);
#   vector<pair<int,int>> events;  
#   int n;
#   cin >> n;
#   while(n--){
#     int l, r;
#     cin >> l >> r;
#     events.push_back({l, 1});
#     events.push_back({r, -1});
#   }
#   sort(events.begin(), events.end());
#   int cnt = 0; // 현재 선의 개수
#   int tot = 0; // 전체 길이(= 답)
#   int loc = -1e9; // 현재 위치
#   for(auto event : events){
#     if(cnt > 0) tot += (event.X - loc);
#     loc = event.X;
#     cnt += event.Y;
#   }
#   cout << tot;
# }
# 4
# 1 3
# 2 5
# 3 5
# 6 7

# #include <bits/stdc++.h>
# using namespace std;
# int main(void) {
#   ios::sync_with_stdio(0);
#   cin.tie(0);
#   int n;
#   cin >> n;
#   vector<pair<int,int>> lines;
#   for (int i=0; i<n; i++){
#     int x, y;
#     cin >> x >> y;
#     lines.push_back({x, y});
#   }
#   sort(lines.begin(), lines.end());
#   int l, r;
#   tie(l, r) = lines[0];
#   int ans = 0;
#   for (int i = 1; i<n; i++) {
#     int a, b;
#     tie(a, b) = lines[i];
#     if (a <= r && b >= r) r = b; // 앞의 선과 겹치는 부분이 있으면 '+' 방향으로 확장
#     else if (a > r) { // 없으면 현재 선의 길이를 더하고, 새로운 선으로 변경
#       ans += r - l;
#       l = a;
#       r = b;
#     }
#   }
#   cout << ans + r - l;
# }