from itertools import combinations_with_replacement

n, m = map(int,input().split())
nums = map(str, sorted((map(int, input().split()))))

for p in combinations_with_replacement(nums, m):
    print(' '.join(p))
