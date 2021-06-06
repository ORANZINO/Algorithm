from itertools import combinations
from math import sqrt


def is_prime(x):
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def solution(nums):
    answer = []
    for c in combinations(nums, 3):
        temp = sum(c)
        if is_prime(temp):
            answer.append(temp)
    return len(answer)

"""
조합으로 3개짜리를 뽑아서 합이 소수가 되면 카운트하고, 아니면 하지 않는다
조합을 활용하고 소수를 체크하는 것만 신경쓰면 되는 문제
"""