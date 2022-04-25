from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer, on_weight = 0, 0
    bridge = deque([0] * bridge_length)
    trucks = deque(truck_weights)
    num_trucks = len(truck_weights)
    finished = 0

    while finished != num_trucks:
        now = bridge.popleft()
        if now != 0:
            finished += 1
            on_weight -= now
        if trucks and on_weight + trucks[0] <= weight:
            temp = trucks.popleft()
            on_weight += temp
            bridge.append(temp)
        else:
            bridge.append(0)
        answer += 1
    return answer

