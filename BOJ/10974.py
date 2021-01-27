from itertools import permutations

n = int(input())
for p in permutations(list(map(str, range(1, n + 1))), n):
    print(' '.join(p))
