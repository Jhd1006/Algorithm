import sys
input = sys.stdin.readline
from collections import deque

n, w, L = map(int, input().split())
a = list(map(int, input().split()))
trucks = deque(a)
bridge = deque([0] * w)
bridge_weight = 0
time = 0


while trucks or bridge_weight > 0:
    time += 1
    truck_out = bridge.popleft()
    bridge_weight -= truck_out
    if trucks and bridge_weight + trucks[0] <= L:
        truck_in = trucks.popleft()
        bridge.append(truck_in)
        bridge_weight += truck_in
    else:
        bridge.append(0)
# n개 트럭 건넘 
# 다리위에는 w대의 트럭
# L은 다리 최대 하중


print(time)