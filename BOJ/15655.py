from itertools import combinations

n, m = map(int,input().split())
nums = map(str, sorted((map(int, input().split()))))

for p in combinations(nums, m):
    print(' '.join(p))
