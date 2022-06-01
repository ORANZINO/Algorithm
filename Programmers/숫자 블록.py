from math import sqrt

def find_num(x):
    if x == 1:
        return 0
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0 and x // i <= 10000000:
            return x // i
    return 1

def solution(begin, end):
    return [find_num(i) for i in range(begin, end + 1)]

