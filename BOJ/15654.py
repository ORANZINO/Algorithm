from itertools import permutations

n, m = map(int,input().split())
nums = map(str, sorted((map(int, input().split()))))

for p in permutations(nums, m):
    print(' '.join(p))
