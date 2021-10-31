def temp(x, n):
    a = x // n
    b = x % n
    if a >= b:
        return a
    else:
        return b


def solution(n, left, right):
    return [temp(i, n) + 1 for i in range(left, right + 1)]



"""
n으로 나누었을 때의 몫과 나머지로 좌표를 알아낸다.
행의 순서 a가 열의 순서 b보다 크거나 같을 때에는 a를, 그렇지 않을 때는 b를 return하여 해당 범위에 맞는 array를 리턴
"""