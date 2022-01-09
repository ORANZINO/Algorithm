from collections import deque


def check(place):
    q = deque()
    steps = [(0, 1), (1, 0), (1, 1), (-1, 1), (2, 0), (0, 2)]
    for i in range(5):
        for j in range(5):
            if place[i][j] == "P":
                for step in steps:
                    x, y = i + step[0], j + step[1]
                    if 0 <= x < 5 and 0 <= y < 5 and place[x][y] == "P":
                        if sum(step) == 1:
                            return 0
                        elif step[1] == 1 and (place[i + step[0]][j] != "X" or place[i][j + step[1]] != "X"):
                            return 0
                        elif (step[0] == 2 or step[1] == 2) and place[i + step[0] // 2][j + step[1] // 2] != "X":
                            return 0

    return 1


def solution(places):
    return [check(place) for place in places]


"""
사람이 있는 경우, 주어진 모든 옵션들을 체크하여 거리두기 여부를 검사한다
"""