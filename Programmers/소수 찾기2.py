from itertools import permutations

def is_prime(x):
    if x == 1 or x == 0:
        return False
    else:
        for i in range(2, (x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True

def solution(numbers):
    nums = list(numbers)
    s = set()
    for i in range(1, len(nums) + 1):
        for p in permutations(nums, i):
            temp = int(''.join(p))
            if is_prime(temp):
                s.add(temp)
    return len(s)
