import sys
input = sys.stdin.readline
from collections import deque

n, w, L = map(int, input().split())
a = deque(map(int, input().split()))
bridge = deque([0]*w)
time = 0
bridge_weight = 0

while a or bridge_weight > 0:
    time += 1
    out = bridge.popleft()
    bridge_weight -= out

    if a and bridge_weight + a[0] <= L:
        truck = a.popleft()
        bridge.append(truck)
        bridge_weight += truck
    else:
        bridge.append(0)

print(time)