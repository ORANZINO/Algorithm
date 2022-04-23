import sys
from collections import defaultdict

sys.setrecursionlimit(1000000)
rooms = defaultdict(int)


def find_next(x):
    if x not in rooms:
        rooms[x] = x + 1
        return x
    else:
        rooms[x] = find_next(rooms[x])
        return rooms[x]


def solution(k, room_number):
    answer = [0] * len(room_number)
    for i, num in enumerate(room_number):
        if num not in rooms:
            answer[i] = num
            rooms[num] = num + 1
        else:
            answer[i] = find_next(num)

    return answer

