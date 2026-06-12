import sys
input = sys.stdin.readline

K, L = map(int, input().split())

d = {}
for i in range(L):
    st_id = input().strip()
    d[st_id] = i

   
sorted_d = sorted(d.items(), key = lambda x : x[1])

idx = 0
while idx < K and idx < len(sorted_d):
    print(sorted_d[idx][0])
    idx += 1