from math import sqrt


def is_prime(x):
    if x == 1:
        return 0
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return 0
    return 1


n = int(input())
nums = list(map(int, input().split()))

print(sum(map(is_prime, nums)))