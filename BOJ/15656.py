from itertools import product

n, m = map(int,input().split())
nums = map(str, sorted((map(int, input().split()))))

for p in product(nums, repeat=m):
    print(' '.join(p))
