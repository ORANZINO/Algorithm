from itertools import permutations

n, m = map(int,input().split())
for c in permutations(map(str, range(1, n + 1)), m):
    print(' '.join(c))
