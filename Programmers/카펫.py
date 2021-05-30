from math import sqrt


def solution(brown, yellow):
    for i in range(1, int(sqrt(yellow)) + 1):
        if yellow % i == 0:
            x = yellow // i + 2
            y = i + 2
            if 2*x + 2*y - 4 == brown:
                return [x, y]


"""
yellow 부분이 직사각형으로 표현된다면,
그 때의 가로 세로 값을 가지고 brown 값이 맞아떨어지는지 확인하면 된다.
맞아떨어지지 않는다면 그 때의 가로 세로 값을 참고하여 return하면 되고,
아니라면 다른 값을 찾아보도록 한다.
"""