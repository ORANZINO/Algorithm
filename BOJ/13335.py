from collections import deque

n, w, L = map(int, input().split())
trucks = deque(map(int, input().split()))
bridge, time = deque([0] * w, maxlen=w), 0

while trucks:
    bridge.popleft()
    if sum(bridge) + trucks[0] <= L:
        bridge.append(trucks.popleft())
    else:
        bridge.append(0)
    time += 1
print(time + w)