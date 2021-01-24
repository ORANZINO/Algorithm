from itertools import combinations
from math import gcd

t = int(input())

for _ in range(t):
    nums = list(map(int, input().split()))
    print(sum([gcd(a, b) for a, b in combinations(nums[1:], 2)]))
