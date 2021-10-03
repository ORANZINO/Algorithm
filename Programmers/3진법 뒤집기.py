def solution(n):
    temp = ''
    while n > 0:
        temp = str(n % 3) + temp
        n //= 3

    return int(temp[::-1], 3)

"""
문제에서 요구한 그대로를 구현하면 되는 문제. 진법 변환을 연습할 수 있었다.
"""