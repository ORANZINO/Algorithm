from math import sqrt


def is_prime(x):
    if x == 1:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def solution(n, k):
    result = ''
    while n:
        result = str(n % k) + result
        n = n // k
    return len(list(num for num in result.split('0') if num and is_prime(int(num))))

